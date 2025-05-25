#!/usr/bin/env python3
"""
Fetch Bluesky posts and convert them to Jekyll markdown files.
"""

import os
import sys
import json
import requests
import re
from datetime import datetime, timezone
from dateutil import parser as date_parser
from pathlib import Path

class BlueskyFetcher:
    def __init__(self):
        self.username = os.getenv('BLUESKY_USERNAME')
        self.password = os.getenv('BLUESKY_PASSWORD')
        self.base_url = 'https://bsky.social/xrpc'
        self.session = None
        self.did = None
        
        if not self.username or not self.password:
            print("❌ BLUESKY_USERNAME and BLUESKY_PASSWORD environment variables required")
            sys.exit(1)
    
    def authenticate(self):
        """Authenticate with Bluesky and get session."""
        try:
            response = requests.post(f"{self.base_url}/com.atproto.server.createSession", 
                                   json={
                                       'identifier': self.username,
                                       'password': self.password
                                   })
            response.raise_for_status()
            
            data = response.json()
            self.session = data['accessJwt']
            self.did = data['did']
            
            print(f"✅ Authenticated as {self.username}")
            return True
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Authentication failed: {e}")
            return False
    
    def fetch_posts(self, limit=20):
        """Fetch recent posts from Bluesky."""
        if not self.session:
            print("❌ Not authenticated")
            return []
        
        headers = {'Authorization': f'Bearer {self.session}'}
        
        try:
            response = requests.get(
                f"{self.base_url}/com.atproto.repo.listRecords",
                headers=headers,
                params={
                    'repo': self.did,
                    'collection': 'app.bsky.feed.post',
                    'limit': limit,
                    'reverse': True  # Most recent first
                }
            )
            response.raise_for_status()
            
            data = response.json()
            posts = data.get('records', [])
            
            print(f"✅ Fetched {len(posts)} posts")
            return posts
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Failed to fetch posts: {e}")
            return []
    
    def clean_text(self, text):
        """Clean text for Jekyll markdown."""
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        
        # Escape Jekyll liquid tags
        text = text.replace('{%', '&#123;%')
        text = text.replace('%}', '%&#125;')
        text = text.replace('{{', '&#123;&#123;')
        text = text.replace('}}', '&#125;&#125;')
        
        return text
    
    def extract_links(self, text, facets=None):
        """Extract and format links from post text."""
        if not facets:
            return text
        
        # Sort facets by byte start position in reverse order
        sorted_facets = sorted(facets, key=lambda f: f.get('index', {}).get('byteStart', 0), reverse=True)
        
        for facet in sorted_facets:
            features = facet.get('features', [])
            index = facet.get('index', {})
            start = index.get('byteStart', 0)
            end = index.get('byteEnd', 0)
            
            for feature in features:
                if feature.get('$type') == 'app.bsky.richtext.facet#link':
                    uri = feature.get('uri', '')
                    if uri:
                        link_text = text[start:end]
                        markdown_link = f"[{link_text}]({uri})"
                        text = text[:start] + markdown_link + text[end:]
                        break
        
        return text
    
    def post_to_markdown(self, post):
        """Convert a Bluesky post to Jekyll markdown."""
        record = post.get('value', {})
        created_at = record.get('createdAt', '')
        text = record.get('text', '')
        facets = record.get('facets', [])
        
        # Parse date
        try:
            post_date = date_parser.isoparse(created_at)
            date_str = post_date.strftime('%Y-%m-%d')
            datetime_str = post_date.strftime('%Y-%m-%d %H:%M:%S %z')
        except:
            date_str = datetime.now().strftime('%Y-%m-%d')
            datetime_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S %z')
        
        # Clean and process text
        clean_text = self.clean_text(text)
        processed_text = self.extract_links(clean_text, facets)
        
        # Create slug from text (first 50 chars, alphanumeric only)
        slug_text = re.sub(r'[^a-zA-Z0-9\s]', '', text[:50])
        slug = re.sub(r'\s+', '-', slug_text.strip()).lower()
        if not slug:
            slug = f"post-{int(post_date.timestamp())}"
        
        # Create filename
        filename = f"{date_str}-{slug}.md"
        
        # Create front matter
        front_matter = f"""---
layout: post
title: "{processed_text[:60]}{'...' if len(processed_text) > 60 else ''}"
date: {datetime_str}
categories: [ideas, bluesky]
tags: [thoughts, bluesky]
bluesky_post: true
source_url: "https://bsky.app/profile/{self.username}/post/{post.get('uri', '').split('/')[-1] if post.get('uri') else ''}"
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