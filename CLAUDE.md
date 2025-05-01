# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build Commands
- Start Jekyll server: `bundle exec jekyll serve --watch`
- Build site: `bundle exec jekyll build`
- Install dependencies: `bundle install`

## Testing
- Preview site locally: http://localhost:4000/

## Code Style Guidelines
- Markdown: Use GitHub Flavored Markdown (GFM)
- YAML: 2-space indentation for _config.yml and front matter
- Front matter required for all posts and pages
- Post filenames: Use format `YYYY-MM-DD-title.md`
- Images should be stored in the `/images` directory
- Line endings: Unix-style (LF)
- Encoding: UTF-8
- Links: Use relative URLs for internal links
- Kramdown: Hard wraps are disabled, use explicit line breaks

## Repository Structure
- `_posts/`: Published posts
- `_drafts/`: Unpublished drafts
- `_layouts/`: Page templates
- `_includes/`: Reusable content
- `_sass/`: SCSS styles
- `images/`: Image assets