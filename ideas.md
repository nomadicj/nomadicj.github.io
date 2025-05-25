---
layout: page
title: Ideas
permalink: /ideas/
description: "Random thoughts and ideas from my Bluesky feed - engineering insights, observations, and musings."
---

# Ideas & Thoughts

A collection of random thoughts, observations, and ideas from my [Bluesky feed](https://bsky.app/profile/{{ site.bluesky.username }}). These are usually shorter-form content that doesn't warrant a full blog post but might spark interesting discussions.

<div class="ideas-feed">
  {% assign bluesky_posts = site.ideas | where: "bluesky_post", true | sort: "date" | reverse %}
  {% assign other_ideas = site.ideas | where: "bluesky_post", nil | sort: "date" | reverse %}
  
  {% if bluesky_posts.size > 0 %}
  <section class="bluesky-ideas">
    <h2>From Bluesky</h2>
    {% for post in bluesky_posts limit: 20 %}
    <article class="idea-post bluesky-post">
      <div class="idea-meta">
        <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %d, %Y" }}</time>
        {% if post.source_url %}
        <a href="{{ post.source_url }}" target="_blank" class="bluesky-link" title="View on Bluesky">
          <svg width="14" height="14" viewBox="0 0 600 530" fill="currentColor">
            <path d="m135.72 44.03c66.496 49.921 138.02 151.14 164.28 205.46 26.262-54.316 97.782-155.54 164.28-205.46 47.98-36.021 125.72-63.892 125.72 24.795 0 17.712-10.155 148.79-16.111 170.07-20.703 73.984-96.144 92.854-163.25 81.433 117.3 19.964 147.14 86.092 82.697 152.22-122.39 125.59-175.91-31.511-189.63-71.766-2.514-7.3797-3.6904-10.832-3.7077-7.8964-0.0174-2.9357-1.1937 0.51669-3.7077 7.8964-13.714 40.255-67.233 197.36-189.63 71.766-64.444-66.128-34.605-132.26 82.697-152.22-67.108 11.421-142.55-7.4491-163.25-81.433-5.9562-21.282-16.111-152.36-16.111-170.07 0-88.687 77.742-60.816 125.72-24.795z"/>
          </svg>
        </a>
        {% endif %}
      </div>
      <div class="idea-content">
        {{ post.content }}
      </div>
    </article>
    {% endfor %}
  </section>
  {% endif %}
  
  {% if other_ideas.size > 0 %}
  <section class="manual-ideas">
    <h2>Earlier Ideas</h2>
    {% for idea in other_ideas %}
    <article class="idea-post manual-post">
      <div class="idea-meta">
        <time datetime="{{ idea.date | date_to_xmlschema }}">{{ idea.date | date: "%b %d, %Y" }}</time>
      </div>
      <div class="idea-content">
        <h3><a href="{{ idea.url }}">{{ idea.title }}</a></h3>
        {% if idea.excerpt %}
        <p>{{ idea.excerpt | strip_html | truncate: 200 }}</p>
        {% endif %}
      </div>
    </article>
    {% endfor %}
  </section>
  {% endif %}
</div>

---

**Follow me on [Bluesky](https://bsky.app/profile/{{ site.bluesky.username }})** for real-time thoughts and discussions.