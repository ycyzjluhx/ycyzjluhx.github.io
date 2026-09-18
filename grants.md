---
layout: default
title: Grants & Fellowships
permalink: /grants/
description: "Research grants and fellowships of Xusheng Zhu."
---

# Grants & Fellowships

<p class="lede">Competitive research support for reconfigurable wireless systems, fluid antennas, intelligent surfaces, and spatial-domain transmission.</p>

<div class="grant-list">
{% for grant in site.data.grants %}
  <article class="grant-card">
    <p class="eyebrow">{{ grant.scheme }}</p>
    <h2>{{ grant.title }}</h2>
    <div class="grant-meta">
      <span><strong>Period:</strong> {{ grant.period }}</span>
      <span><strong>Role:</strong> {{ grant.role }}</span>
      <span><strong>Funding:</strong> {{ grant.amount }}</span>
      {% if grant.project_id %}<span><strong>Project ID:</strong> {{ grant.project_id }}</span>{% endif %}
    </div>
    {% if grant.description %}<p>{{ grant.description }}</p>{% endif %}
  </article>
{% endfor %}
</div>

## Selected Honors

- **Shanghai Outstanding Graduate**, Shanghai Jiao Tong University, Top 1%, provincial level, 2025.
- **Shangjun Scholarship**, Shanghai Jiao Tong University, Top 3%, 2025.
- **National Scholarship**, Shanghai Jiao Tong University, Top 1%, national level, 2024.
- **Second Prize, Excellent Annual Conference Paper**, Shanghai Institute of Communications, 2024.
