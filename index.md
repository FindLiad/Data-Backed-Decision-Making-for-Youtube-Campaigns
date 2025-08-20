---
layout: default
title: Data-Backed Decision Making for YouTube Campaigns
---

{% comment %}
Render README.md starting at "## Summary", then split again at
"## Table of Contents" so we can inject the mobile Author Card
RIGHT AFTER the Summary section and BEFORE the TOC.
{% endcomment %}

{% capture readme_raw %}{% include_relative README.md %}{% endcapture %}

{%- assign summary_split = readme_raw | split: '## Summary' -%}
{%- if summary_split.size > 1 -%}
  {%- capture after_summary -%}## Summary{{ summary_split[1] }}{%- endcapture -%}
{%- else -%}
  {%- assign after_summary = readme_raw -%}
{%- endif -%}

{%- assign toc_split = after_summary | split: '## Table of Contents' -%}
{%- if toc_split.size > 1 -%}
  {{ toc_split[0] | markdownify }}

  <!-- ===== Mobile/Compressed-Desktop Author Card (injected after Summary) ===== -->
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

  {%- capture toc_and_after -%}## Table of Contents{{ toc_split[1] }}{%- endcapture -%}
  {{ toc_and_after | markdownify }}
{%- else -%}
  {{ after_summary | markdownify }}
  <!-- Fallback: still inject the mobile card if no TOC was found -->
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
