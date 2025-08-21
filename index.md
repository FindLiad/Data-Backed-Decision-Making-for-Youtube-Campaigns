---
layout: default
title: Data-Backed Decision Making for YouTube Campaigns
---

{% comment %}
Show README starting at the CAR "Summary" section (or fallback to generic "## Summary"),
then split at "## Table of Contents". Convert any inline Back-to-top blocks to .car-backlink
and inject a mobile-only About card with Back-to-top links before and after it.
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

{%- comment -%} normalize Back-to-top anchors {%- endcomment -%}
{% capture back_orig_site %}<div align="right"><a href="#site-top">↑ Back to top</a></div>{% endcapture %}
{% capture back_orig_toc  %}<div align="right"><a href="#table-of-contents">↑ Back to top</a></div>{% endcapture %}
{% capture back_classed   %}<div class="car-backlink" align="right"><a href="#site-top">↑ Back to top</a></div>{% endcapture %}

{% if toc_split.size > 1 %}
  {% assign pre = toc_split[0] | replace: back_orig_site, back_classed | replace: back_orig_toc, back_classed %}
  {{ pre | markdownify }}

  <!-- Mobile/compact-only: Back to top BETWEEN Summary and About -->
  <div class="backlink--injected" align="right"><a href="#site-top">↑ Back to top</a></div>

  <!-- Mobile/compact-only About the Author -->
  <div class="author-card author-card--mobile">
    <div class="author-card__heading">About the Author</div>

    <a href="{{ site.author_photo }}" target="_blank" rel="noopener">
      <img class="author-card__photo" src="{{ site.author_photo }}" alt="{{ site.author }}">
    </a>

    <div class="author-card__name">{{ site.author }}</div>
    {% if site.author_title %}<div class="author-card__title">{{ site.author_title }}</div>{% endif %}
    {% if site.author_subtitle %}<div class="author-card__subtitle">{{ site.author_subtitle }}</div>{% endif %}

    <div class="author-card__links">
      {% for l in site.author_links %}
        <a class="author-card__btn" href="{{ l.url | escape }}" target="_blank" rel="noopener noreferrer">
          {{ l.icon }} {{ l.label }}
        </a>
      {% endfor %}
    </div>
  </div>

  <!-- Mobile/compact-only: Back to top AFTER About -->
  <div class="backlink--after-author" align="right"><a href="#site-top">↑ Back to top</a></div>

  {% capture rest %}## Table of Contents{{ toc_split[1] }}{% endcapture %}
  {{ rest | markdownify }}
{% else %}
  {% assign pre = body_from_start | replace: back_orig_site, back_classed | replace: back_orig_toc, back_classed %}
  {{ pre | markdownify }}

  <div class="backlink--injected" align="right"><a href="#site-top">↑ Back to top</a></div>

  <div class="author-card author-card--mobile">
    <div class="author-card__heading">About the Author</div>

    <a href="{{ site.author_photo }}" target="_blank" rel="noopener">
      <img class="author-card__photo" src="{{ site.author_photo }}" alt="{{ site.author }}">
    </a>

    <div class="author-card__name">{{ site.author }}</div>
    {% if site.author_title %}<div class="author-card__title">{{ site.author_title }}</div>{% endif %}
    {% if site.author_subtitle %}<div class="author-card__subtitle">{{ site.author_subtitle }}</div>{% endif %}

    <div class="author-card__links">
      {% for l in site.author_links %}
        <a class="author-card__btn" href="{{ l.url | escape }}" target="_blank" rel="noopener noreferrer">
          {{ l.icon }} {{ l.label }}
        </a>
      {% endfor %}
    </div>
  </div>

  <div class="backlink--after-author" align="right"><a href="#site-top">↑ Back to top</a></div>
{% endif %}
