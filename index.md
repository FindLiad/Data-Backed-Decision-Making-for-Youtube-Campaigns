---
layout: default
title: Data-Backed Decision Making for YouTube Campaigns
---

{% comment %}
Show README starting at the CAR "Summary" section, then inject a mobile
About card BEFORE the Table of Contents.
We accept either the explicit CAR heading or the generic "## Summary".
{% endcomment %}

{% capture readme_raw %}{% include_relative README.md %}{% endcapture %}

{%- assign token_car = '## A time I went above and beyond to deliver for the customer' -%}
{%- assign token_summary = '## Summary' -%}

{%- if readme_raw contains token_car -%}
  {%- assign start_token = token_car -%}
{%- else -%}
  {%- assign start_token = token_summary -%}
{%- endif -%}

{%- assign after_start = readme_raw | split: start_token -%}
{%- if after_start.size > 1 -%}
  {%- capture body_from_start -%}{{ start_token }}{{ after_start[1] }}{%- endcapture -%}
{%- else -%}
  {%- assign body_from_start = readme_raw -%}
{%- endif -%}

{%- assign toc_split = body_from_start | split: '## Table of Contents' -%}
{%- if toc_split.size > 1 -%}
  {{ toc_split[0] | markdownify }}

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

  {%- capture toc_and_rest -%}## Table of Contents{{ toc_split[1] }}{%- endcapture -%}
  {{ toc_and_rest | markdownify }}
{%- else -%}
  {{ body_from_start | markdownify }}
  <!-- Fallback injection if no TOC present -->
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
{%- endif -%}
