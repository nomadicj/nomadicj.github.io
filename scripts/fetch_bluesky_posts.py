#!/usr/bin/env python3
"""
Fetch Bluesky posts and convert them to Jekyll markdown files.
"""

import os
import sys
import json
import re
from datetime import datetime, timezone
from dateutil import parser as date_parser
from pathlib import Path

try:
    from atproto import Client
except ImportError:
    print("❌ atproto library not installed. Run: pip install atproto")
    sys.exit(1)

class BlueskyFetcher:
    def __init__(self):
        self.username = os.getenv('BLUESKY_USERNAME')
        self.password = os.getenv('BLUESKY_PASSWORD')
        self.client = None
        
        if not self.username or not self.password:
            print("❌ BLUESKY_USERNAME and BLUESKY_PASSWORD environment variables required")
            sys.exit(1)
    
    def authenticate(self):
        """Authenticate with Bluesky using AT Protocol."""
        try:
            self.client = Client()
            self.client.login(self.username, self.password)
            
            print(f"✅ Authenticated as {self.username}")
            return True
            
        except Exception as e:
            print(f"❌ Authentication failed: {e}")
            return False
    
    def fetch_posts(self, limit=20):
        """Fetch recent posts from Bluesky."""
        if not self.client:
            print("❌ Not authenticated")
            return []
        
        try:
            # Get the user's profile to get their DID
            profile = self.client.get_profile(self.username)
            did = profile.did
            
            # Fetch posts from the user's feed
            response = self.client.get_author_feed(
                actor=did,
                limit=limit
            )
            
            posts = []
            for item in response.feed:
                if hasattr(item, 'post') and item.post.author.did == did:
                    posts.append(item.post)
            
            print(f"✅ Fetched {len(posts)} posts")
            return posts
            
        except Exception as e:
            print(f"❌ Failed to fetch posts: {e}")
            return []
    
    def clean_text(self, text):
        """Clean text for Jekyll markdown."""
        if not text:
            return ""
            
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        
        # Escape Jekyll liquid tags
        text = text.replace('{%', '&#123;%')
        text = text.replace('%}', '%&#125;')
        text = text.replace('{{', '&#123;&#123;')
        text = text.replace('}}', '&#125;&#125;')
        
        return text
    
    def extract_links(self, post):
        """Extract and format links from post."""
        text = post.record.text
        
        # Check for facets (rich text features like links)
        if hasattr(post.record, 'facets') and post.record.facets:
            # Sort facets by byte start position in reverse order
            sorted_facets = sorted(
                post.record.facets, 
                key=lambda f: f.index.byte_start, 
                reverse=True
            )
            
            for facet in sorted_facets:
                for feature in facet.features:
                    if hasattr(feature, 'uri'):  # It's a link
                        start = facet.index.byte_start
                        end = facet.index.byte_end
                        link_text = text[start:end]
                        markdown_link = f"[{link_text}]({feature.uri})"
                        text = text[:start] + markdown_link + text[end:]
                        break
        
        return text
    
    def post_to_markdown(self, post):
        """Convert a Bluesky post to Jekyll markdown."""
        # Extract post data
        created_at = post.record.created_at
        text = getattr(post.record, 'text', '')
        
        # Parse date
        try:
            if isinstance(created_at, str):
                post_date = date_parser.isoparse(created_at)
            else:
                post_date = created_at
            
            date_str = post_date.strftime('%Y-%m-%d')
            datetime_str = post_date.strftime('%Y-%m-%d %H:%M:%S %z')
        except:
            date_str = datetime.now().strftime('%Y-%m-%d')
            datetime_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S %z')
        
        # Clean and process text
        clean_text = self.clean_text(text)
        processed_text = self.extract_links(post)
        processed_text = self.clean_text(processed_text)
        
        # Create slug from text (first 50 chars, alphanumeric only)
        slug_text = re.sub(r'[^a-zA-Z0-9\s]', '', text[:50])
        slug = re.sub(r'\s+', '-', slug_text.strip()).lower()
        if not slug:
            slug = f"post-{int(post_date.timestamp())}"
        
        # Create filename
        filename = f"{date_str}-{slug}.md"
        
        # Get post URI for linking back to Bluesky
        post_uri = post.uri if hasattr(post, 'uri') else ''
        post_id = post_uri.split('/')[-1] if post_uri else ''
        source_url = f"https://bsky.app/profile/{self.username}/post/{post_id}" if post_id else ""
        
        # Create front matter
        title = processed_text[:60] + ('...' if len(processed_text) > 60 else '')
        title = title.replace('"', '\\"')  # Escape quotes in title
        
        front_matter = f"""---
layout: post
title: "{title}"
date: {datetime_str}
categories: [ideas, bluesky]
tags: [thoughts, bluesky]
bluesky_post: true
source_url: "{source_url}"
---

{processed_text}
"""
        
        return filename, front_matter
    
    def save_posts(self, posts):
        """Save posts as Jekyll markdown files."""
        ideas_dir = Path('_ideas')
        ideas_dir.mkdir(exist_ok=True)
        
        saved_count = 0
        
        for post in posts:
            try:
                filename, content = self.post_to_markdown(post)
                file_path = ideas_dir / filename
                
                # Don't overwrite existing files
                if file_path.exists():
                    continue
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                saved_count += 1
                print(f"✅ Saved: {filename}")
                
            except Exception as e:
                print(f"❌ Failed to save post: {e}")
                continue
        
        print(f"💾 Saved {saved_count} new posts")
        return saved_count

def main():
    print("🦋 Starting Bluesky fetch...")
    
    fetcher = BlueskyFetcher()
    
    if not fetcher.authenticate():
        sys.exit(1)
    
    posts = fetcher.fetch_posts(limit=50)  # Fetch more to account for duplicates
    
    if posts:
        saved = fetcher.save_posts(posts)
        print(f"🎉 Process complete! {saved} new ideas added.")
    else:
        print("❌ No posts to process")

if __name__ == '__main__':
    main()