---
layout: home
title: Home
permalink: /
role: "Marie Skłodowska-Curie Actions Postdoctoral Fellow"
affiliation: "Department of Electronic & Electrical Engineering, University College London"
research_statement: "I develop reconfigurable wireless technologies for 6G, with a focus on fluid and movable antennas, intelligent surfaces, spatial/index modulation, and AI-assisted wireless systems."
profile_image: "/assets/img/profile.jpg"
description: "Academic homepage of Xusheng Zhu, MSCA Postdoctoral Fellow at UCL, working on 6G wireless communications and reconfigurable wireless systems."
---

## About

I am a **Marie Skłodowska-Curie Actions Postdoctoral Fellow** in the Department of Electronic & Electrical Engineering at **University College London (UCL)**. I received the Ph.D. degree in Information and Communication Engineering from **Shanghai Jiao Tong University** in 2025. My research focuses on reconfigurable wireless systems for 6G, with particular interests in fluid and movable antennas, reconfigurable intelligent surfaces, spatial/index modulation, and AI-assisted wireless communications.

My work has appeared in journals including *IEEE Journal on Selected Areas in Communications*, *IEEE Transactions on Wireless Communications*, and *IEEE Transactions on Communications*. I also contribute to the community through IEEE journal editorships, guest editing, and international conference leadership.

## Research Highlights

<div class="grid grid-4">
  <article class="card highlight-card">
    <h3>Fluid & Movable Antennas</h3>
    <p>Spatially reconfigurable antenna systems, performance limits, port selection, URLLC, UAV links, and prototype-aware design.</p>
  </article>
  <article class="card highlight-card">
    <h3>Intelligent Surfaces</h3>
    <p>RIS/FRIS architectures, transmissive surfaces, secure transmission, beamforming, and programmable propagation.</p>
  </article>
  <article class="card highlight-card">
    <h3>Spatial / Index Modulation</h3>
    <p>Space shift keying, spatial modulation, spatial scattering modulation, detectors, optimization, and error analysis.</p>
  </article>
  <article class="card highlight-card">
    <h3>AI-Assisted Wireless</h3>
    <p>Learning-assisted control, model-driven learning, GNN/RL methods, and autonomous reconfiguration for 6G systems.</p>
  </article>
</div>

<p><a href="{{ '/research/' | relative_url }}">Explore research themes →</a></p>

## Selected Publications
{% assign home_publications = site.data.publications.selected | slice: 0, 7 %}
{% include publication-list.html items=home_publications %}
<p><a href="{{ '/publications/' | relative_url }}">View all publications →</a></p>

## Recent News
<ul class="news-list">
{% for post in site.posts limit:4 %}
  <li class="news-item">
    <time class="news-date" datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %Y" }}</time>
    <div>
      <h3 class="news-title"><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
      <p>{{ post.excerpt | strip_html | truncatewords: 26 }}</p>
    </div>
  </li>
{% endfor %}
</ul>
<p><a href="{{ '/news/' | relative_url }}">More news →</a></p>

## Academic Service Highlights

<ul class="service-list">
  <li><span class="service-role">Editor</span>, <strong>IEEE Transactions on Communications</strong>, Communication Theory & Systems II.</li>
  <li><span class="service-role">Associate Editor</span>, <strong>IEEE Wireless Communications Letters</strong>, <strong>IEEE Communications Letters</strong>, and <strong>IEEE Open Journal of the Communications Society</strong>.</li>
  <li><span class="service-role">Guest Editor</span>, <strong>IEEE Transactions on Aerospace and Electronic Systems</strong> Special Section on Next-Generation Reconfigurable Antenna Systems for Aerospace Communications and Sensing.</li>
  <li><span class="service-role">Symposium Co-Chair</span>, <strong>AIPIP 2026</strong>, Intelligent Antennas, Reconfigurable Electromagnetic Technologies, and High-Frequency Links.</li>
  <li><span class="service-role">Workshop leadership</span> at <strong>IEEE GLOBECOM 2026</strong>, <strong>IEEE/CIC ICCC 2026</strong>, and <strong>IEEE VTC 2026-Spring</strong>.</li>
</ul>
<p><a href="{{ '/service/' | relative_url }}">View academic service →</a></p>

## Selected Grants & Fellowships

<div class="grid grid-3">
{% for grant in site.data.grants %}
  <article class="card">
    <p class="eyebrow">{{ grant.period }}</p>
    <h3>{{ grant.title }}</h3>
    <p>{{ grant.scheme }}</p>
    <p class="muted">{{ grant.role }} · {{ grant.amount }}</p>
  </article>
{% endfor %}
</div>
<p><a href="{{ '/grants/' | relative_url }}">View grants & fellowships →</a></p>
