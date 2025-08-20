---
layout: default
title: Data-Backed Decision Making for YouTube Campaigns
---

{% comment %}
Show README starting at the CAR "Summary" section (or fallback to generic "## Summary"),
then split at "## Table of Contents". We convert the CAR's inline Back-to-top into a
classed element (car-backlink) so CSS can toggle it off on mobile/compact. We then inject
a second Back-to-top AFTER the mobile author card (backlink--injected).
{% endcomment %}

{% capture readme_raw %}{% include_relative README.md %}{% endcapture %}

{% assign token_car = '## A time I went above and beyond to deliver for the customer' %}
{% assign token_summary = '## Summary' %}

{% if readme_raw contains token_car %}
  {% assign start_token = token_car %}
{% else %}
  {% assign start_token = token_summary %}
{% endif %}

{% assign after_start = readme_raw | split: start_token %}
{% if after_start.size > 1 %}
  {% capture body_from_start %}{{ start_token }}{{ after_start[1] }}{% endcapture %}
{% else %}
  {% assign body_from_start = readme_raw %}
{% endif %}

{% assign toc_split = body_from_start | split: '## Table of Contents' %}

{% capture back_orig %}<div align="right"><a href="#table-of-contents">↑ Back to top</a></div>{% endcapture %}
{% capture back_classed %}<div class="car-backlink" align="right"><a href="#table-of-contents">↑ Back to top</a></div>{% endcapture %}

{% if toc_split.size > 1 %}
  {% assign car_with_class = toc_split[0] | replace: back_orig, back_classed %}
  {{ car_with_class | markdownify }}

  <!-- ===== Mobile/Compressed-Desktop Author Card (AFTER CAR, BEFORE TOC) ===== -->
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

  <!-- Back to top shown only on mobile/compact via CSS -->
  <div class="backlink--injected" align="right">
    <a href="#table-of-contents">↑ Back to top</a>
  </div>

  {% capture toc_and_rest %}## Table of Contents{{ toc_split[1] }}{% endcapture %}
  {{ toc_and_rest | markdownify }}
{% else %}
  {% assign car_with_class = body_from_start | replace: back_orig, back_classed %}
  {{ car_with_class | markdownify }}

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

  <div class="backlink--injected" align="right">
    <a href="#table-of-contents">↑ Back to top</a>
  </div>
{% endif %}


