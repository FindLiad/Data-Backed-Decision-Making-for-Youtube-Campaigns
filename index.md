---
layout: default
title: Data-Backed Decision Making for YouTube Campaigns
---

{% comment %}
Render README.md but drop everything before the first "## Summary".
Then inject a mobile-only Author Card AFTER the Summary (so it shows below the CAR section on mobile).
{% endcomment %}

{% capture readme_raw %}{% include_relative README.md %}{% endcapture %}
{% assign split_token = '## Summary' %}
{% assign parts = readme_raw | split: split_token %}
{% if parts.size > 1 %}
  {% capture after %}{{ split_token }}{{ parts[1] }}{% endcapture %}
  {{ after | markdownify }}
{% else %}
  {{ readme_raw | markdownify }}
{% endif %}

<!-- ===== Mobile-only Author Card injected AFTER the summary/content ===== -->
<div class="author-card author-card--mobile">
  <div class="author-card__heading">About the Author</div>

  <a href="{{ site.author_photo }}" target="_blank" rel="noopener">
    <img class="author-card__photo" src="{{ site.author_photo }}" alt="{{ site.author }}">
  </a>

  <div class="author-card__name">{{ site.author }}</div>
  {% if site.author_title %}
    <div class="author-card__title">{{ site.author_title }}</div>
  {% endif %}
  {% if site.author_subtitle %}
    <div class="author-card__subtitle">{{ site.author_subtitle }}</div>
  {% endif %}

  <div class="author-card__links">
    {% for l in site.author_links %}
      <a class="author-card__btn" href="{{ l.url | escape }}" target="_blank" rel="noopener noreferrer">
        {{ l.icon }} {{ l.label }}
      </a>
    {% endfor %}
  </div>
</div>
