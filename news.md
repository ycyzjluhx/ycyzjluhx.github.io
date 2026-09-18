---
layout: default
title: News
permalink: /news/
description: "Recent academic news, appointments, publications, and conference activities of Xusheng Zhu."
---

# News

<p class="lede">Recent research, editorial, conference, and professional updates.</p>

<ul class="news-list">
{% for post in site.posts %}
  <li class="news-item">
    <time class="news-date" datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%d %b %Y" }}</time>
    <div>
      <h2 class="news-title"><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
      <p>{{ post.excerpt | strip_html | truncatewords: 42 }}</p>
    </div>
  </li>
{% endfor %}
</ul>
