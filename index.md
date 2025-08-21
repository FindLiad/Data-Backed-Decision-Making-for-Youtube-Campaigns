---
layout: default
title: Data-Backed Decision Making for YouTube Campaigns
---

{%- comment -%}
Render README starting at the Summary/CAR section, then split at "## Table of Contents".
We convert the README's inline Back-to-top into a classed element (.car-backlink).
We also inject a mobile-only About card and two mobile-only back-to-top links.
Desktop hides those injected elements via CSS so there is NEVER a second About on desktop.
{%- endcomment -%}

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
  {% capture from_start %}{{ start_token }}{{ after_start[1] }}{% endcapture %}
{% else %}
  {% assign from_start = readme_raw %}
{% endif %}

{% assign toc_parts = from_start | split: '## Table of Contents' %}
{% assign pre_toc = toc_parts[0] %}
{% assign post_toc = toc_parts[1] %}

{%- comment -%} Normalize any inline "Back to top" to a classed element. {%- endcomment -%}
{%- capture back_orig -%}<div align="right"><a href="#site-top">↑ Back to top</a></div>{%- endcapture -%}
{%- capture back_classed -%}<div class="car-backlink" align="right"><a href="#site-top">↑ Back to top</a></div>{%- endcapture -%}
{% assign pre_toc = pre_toc | replace: back_orig, back_classed %}

{{ pre_toc | markdownify }}

{%- comment -%}
The following three blocks are **mobile/compact-only**. CSS hides them on wide/desktop,
so desktop will NOT show a second About nor an extra Back-to-top.
{%- endcomment -%}

<!-- Mobile/compact-only Back to top BETWEEN Summary and About -->
<div class="backlink--injected" align="right"><a href="#site-top">↑ Back to top</a></div>
<hr class="m-divider" />

<!-- Mobile/compact-only About the Author -->
<div class="author-card author-card--mobile">
  <div class="author-card__heading">About the Author</div>

  <a href="{{ site.author_photo }}" target="_blank" rel="noopener">
    <img class="author-card__photo" src="{{ site.author_photo }}" alt="{{ site.author }}">
  </a>

  <div class="author-card__name">{{ site.author }}</div>
  {% if site.author_title %}
    <div class="author-card__title"><em>{{ site.author_title }}</em></div>
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

<!-- Mobile/compact-only Back to top AFTER About -->
<div class="backlink--after-author" align="right"><a href="#site-top">↑ Back to top</a></div>

{% if post_toc %}
  {% capture rest %}## Table of Contents{{ post_toc }}{% endcapture %}
  {{ rest | markdownify }}
{% endif %}


