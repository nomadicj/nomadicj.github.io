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
            
            # Process posts to combine threads
            processed_posts = self.combine_threads(posts)
            print(f"✅ Processed into {len(processed_posts)} posts (threads combined)")
            
            return processed_posts
            
        except Exception as e:
            print(f"❌ Failed to fetch posts: {e}")
            return []
    
    def remove_duplicates(self, posts):
        """Remove duplicate posts based on content similarity and timing."""
        unique_posts = []
        seen_content = set()
        
        # Sort posts by creation time
        sorted_posts = sorted(posts, key=lambda p: p.record.created_at)
        
        for post in sorted_posts:
            text = getattr(post.record, 'text', '').strip()
            
            # Create a normalized version for comparison
            normalized_text = self.normalize_text_for_comparison(text)
            
            # Check for exact duplicates
            if normalized_text in seen_content:
                print(f"🗑️ Removing duplicate post: {text[:50]}...")
                continue
            
            # Check for substantial overlap with recent posts
            is_duplicate = False
            for existing_text in seen_content:
                if self.texts_are_similar(normalized_text, existing_text):
                    print(f"🗑️ Removing similar post: {text[:50]}...")
                    is_duplicate = True
                    break
            
            if not is_duplicate:
                seen_content.add(normalized_text)
                unique_posts.append(post)
        
        return unique_posts
    
    def normalize_text_for_comparison(self, text):
        """Normalize text for duplicate detection."""
        import re
        # Remove extra whitespace, convert to lowercase
        normalized = re.sub(r'\s+', ' ', text.lower().strip())
        # Remove common thread indicators for comparison
        normalized = self.clean_thread_indicators(normalized)
        return normalized
    
    def texts_are_similar(self, text1, text2, threshold=0.8):
        """Check if two texts are substantially similar."""
        if not text1 or not text2:
            return False
        
        # Simple similarity check based on common words
        words1 = set(text1.split())
        words2 = set(text2.split())
        
        if len(words1) == 0 or len(words2) == 0:
            return False
        
        # Calculate Jaccard similarity
        intersection = len(words1.intersection(words2))
        union = len(words1.union(words2))
        
        similarity = intersection / union if union > 0 else 0
        return similarity >= threshold
    
    def combine_threads(self, posts):
        """Combine threaded posts into single coherent posts."""
        thread_map = {}
        standalone_posts = []
        processed_posts = set()  # Track which posts we've already processed
        
        # First pass: Remove duplicate posts
        posts = self.remove_duplicates(posts)
        
        # Build thread relationships
        for post in posts:
            if post.uri in processed_posts:
                continue
            post_text = getattr(post.record, 'text', '')
            
            # Check if this is a reply to another post
            reply = getattr(post.record, 'reply', None)
            if reply and hasattr(reply, 'parent'):
                parent_uri = reply.parent.uri
                
                # Check if parent is from the same author (thread continuation)
                try:
                    # Extract the parent post ID and check if it's from our posts
                    parent_in_our_posts = any(p.uri == parent_uri for p in posts)
                    
                    if parent_in_our_posts:
                        # This is part of a thread
                        if parent_uri not in thread_map:
                            thread_map[parent_uri] = []
                        thread_map[parent_uri].append(post)
                    else:
                        # Reply to someone else's post, treat as standalone
                        standalone_posts.append(post)
                except:
                    # If we can't determine, treat as standalone
                    standalone_posts.append(post)
            else:
                # Check if this post starts a thread by looking for common thread indicators
                if self.is_thread_starter(post_text):
                    # This might be a thread starter
                    thread_followers = self.find_thread_followers(post, posts)
                    if thread_followers:
                        # Create a combined thread post
                        combined_post = self.create_combined_thread_post(post, thread_followers)
                        standalone_posts.append(combined_post)
                        # Mark all thread posts as processed
                        processed_posts.add(post.uri)
                        for follower in thread_followers:
                            processed_posts.add(follower.uri)
                    else:
                        standalone_posts.append(post)
                else:
                    # This is a standalone post
                    standalone_posts.append(post)
                    processed_posts.add(post.uri)
        
        # Process thread_map to create combined posts
        for parent_uri, replies in thread_map.items():
            # Find the parent post
            parent_post = next((p for p in posts if p.uri == parent_uri), None)
            if parent_post:
                combined_post = self.create_combined_thread_post(parent_post, replies)
                standalone_posts.append(combined_post)
        
        return standalone_posts
    
    def is_thread_starter(self, text):
        """Check if a post looks like it starts a thread."""
        thread_indicators = [
            '🧵', 'thread', '1/', '1 of', '1|', 'part 1',
            'continued below', 'more in replies', '👇'
        ]
        text_lower = text.lower()
        return any(indicator in text_lower for indicator in thread_indicators)
    
    def find_thread_followers(self, starter_post, all_posts):
        """Find posts that follow the starter post in a thread."""
        followers = []
        starter_time = starter_post.record.created_at
        
        # Look for posts that reply to the starter or mention thread continuation
        for post in all_posts:
            if post.uri == starter_post.uri:
                continue
                
            # Check if it's a reply to the starter
            reply = getattr(post.record, 'reply', None)
            if reply and hasattr(reply, 'parent') and reply.parent.uri == starter_post.uri:
                followers.append(post)
                continue
            
            # Check for thread numbering patterns in posts after the starter
            post_time = post.record.created_at
            if post_time > starter_time:  # Posted after starter
                text = getattr(post.record, 'text', '').lower()
                if any(pattern in text for pattern in ['2/', '3/', '4/', '5/', 'part 2', 'part 3']):
                    followers.append(post)
        
        # Sort followers by creation time
        followers.sort(key=lambda p: p.record.created_at)
        return followers
    
    def create_combined_thread_post(self, starter_post, follower_posts):
        """Create a thread post with structured content."""
        # Create thread structure
        thread_parts = []
        
        # Add starter post
        starter_text = getattr(starter_post.record, 'text', '')
        starter_text = self.clean_thread_indicators(starter_text)
        if starter_text.strip():
            thread_parts.append({
                'text': starter_text,
                'order': 1,
                'uri': starter_post.uri,
                'created_at': starter_post.record.created_at
            })
        
        # Add follower posts
        for i, post in enumerate(follower_posts, 2):
            follower_text = getattr(post.record, 'text', '')
            follower_text = self.clean_thread_indicators(follower_text)
            if follower_text.strip():
                thread_parts.append({
                    'text': follower_text,
                    'order': i,
                    'uri': post.uri,
                    'created_at': post.record.created_at
                })
        
        # Store thread structure in the post
        starter_post._thread_parts = thread_parts
        starter_post._is_thread = True  # Mark as thread
        
        return starter_post
    
    def clean_thread_indicators(self, text):
        """Remove common thread indicators from text."""
        import re
        
        # Remove thread numbering patterns
        patterns = [
            r'^\d+[/|]\d*\s*',  # 1/5, 2/, etc at start
            r'^\d+\s*of\s*\d+\s*',  # 1 of 5, etc
            r'part\s*\d+\s*[:-]?\s*',  # part 1:, part 2, etc
            r'🧵\s*',  # thread emoji
            r'thread\s*[:-]?\s*',  # "thread:" or "thread"
            r'continued\s+below\s*',
            r'more\s+in\s+replies\s*',
            r'👇\s*'
        ]
        
        for pattern in patterns:
            text = re.sub(pattern, '', text, flags=re.IGNORECASE)
        
        return text.strip()
    
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
        # Handle threaded vs single posts differently
        if hasattr(post, '_is_thread') and post._is_thread:
            # This is a threaded post
            first_part = post._thread_parts[0] if post._thread_parts else {}
            first_text = first_part.get('text', '')
            
            # Try to extract the main topic from the first sentence
            first_sentence = first_text.split('.')[0].split('\n')[0] if first_text else ''
            title = first_sentence[:60] + ('...' if len(first_sentence) > 60 else '')
            if not title.strip():
                title = "Thread: " + first_text[:50] + ('...' if len(first_text) > 50 else '')
            
            title = title.replace('"', '\\"')  # Escape quotes in title
            
            # Create YAML for thread parts
            thread_yaml = "thread_parts:\n"
            for part in post._thread_parts:
                part_text = part['text'].replace('"', '\\"').replace('\n', '\\n')
                thread_yaml += f"""  - order: {part['order']}
    text: "{part_text}"
    uri: "{part['uri']}"
"""
            
            front_matter = f"""---
layout: post
title: "{title}"
date: {datetime_str}
categories: [ideas, bluesky]
tags: [thoughts, bluesky]
bluesky_post: true
is_thread: true
source_url: "{source_url}"
{thread_yaml}---

<!-- Thread content is rendered from thread_parts in front matter -->
"""
        else:
            # Single post
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