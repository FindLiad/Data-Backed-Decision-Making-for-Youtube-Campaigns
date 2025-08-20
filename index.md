---
layout: default
title: Data-Backed Decision Making for YouTube Campaigns
---

{% comment %}
Render README starting at our CAR "Summary" section (or fallback to generic "## Summary").
Then split at "## Table of Contents". We remove the built-in “Back to top” at the
end of the CAR block and reinsert it **after** the injected mobile Author Card,
so on mobile/compressed desktop the link appears below the author—matching Project 2.
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

{%- capture back_markup -%}<div align="right"><a href="#table-of-contents">↑ Back to top</a></div>{%- endcapture -%}

{%- if toc_split.size > 1 -%}
  {%- assign car_without_bt = toc_split[0] | replace: back_markup, '' -%}
  {{ car_without_bt | markdownify }}

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

  <!-- Re-insert “Back to top” AFTER the mobile author card -->
  {{ back_markup }}

  {%- capture toc_and_rest -%}## Table of Contents{{ toc_split[1] }}{%- endcapture -%}
  {{ toc_and_rest | markdownify }}
{%- else -%}
  {%- assign car_without_bt = body_from_start | replace: back_markup, '' -%}
  {{ car_without_bt | markdownify }}

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

  {{ back_markup }}
{%- endif -%}

