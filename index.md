---
layout: default
title: Data-Backed Decision Making for YouTube Campaigns
---

{% comment %}
Project 1 index — mirrors Project 2 behavior/architecture.

Flow:
1) Read README.md
2) Start rendering from the first matching CAR/Summary token
3) Split at "## Table of Contents"
4) Normalize inline Back-to-top → .car-backlink
5) Inject mobile-only Back-to-top + mobile-only Author card
6) Append the original Table of Contents (if present)

Desktop CSS should hide the injected mobile bits so there is NEVER a second About on desktop.
{% endcomment %}

{% capture readme_raw %}{% include_relative README.md %}{% endcapture %}

{%- assign token1 = '## How I balanced Business Requirements vs. Customer Needs' -%}
{%- assign token2 = '## Business Requirements vs. Customer Needs' -%}
{%- assign token3 = '## A time I went above and beyond to deliver for the customer' -%}
{%- assign token4 = '## Summary' -%}

{%- if readme_raw contains token1 -%}
  {%- assign start_token = token1 -%}
{%- elsif readme_raw contains token2 -%}
  {%- assign start_token = token2 -%}
{%- elsif readme_raw contains token3 -%}
  {%- assign start_token = token3 -%}
{%- else -%}
  {%- assign start_token = token4 -%}
{%- endif -%}

{%- assign after_start = readme_raw | split: start_token -%}
{%- if after_start.size > 1 -%}
  {%- capture from_car %}{{ start_token }}{{ after_start[1] }}{% endcapture %}
{%- else -%}
  {%- assign from_car = readme_raw -%}
{%- endif -%}

{%- assign toc_parts = from_car | split: '## Table of Contents' -%}
{%- assign pre_toc = toc_parts[0] -%}
{%- assign post_toc = toc_parts[1] -%}

{%- comment -%} Strip any previously injected mobile author card (idempotent). {%- endcomment -%}
{%- assign strip_marker = '<!-- ===== Mobile-only Author Card injected AFTER the story section ===== -->' -%}
{%- if pre_toc contains strip_marker -%}
  {%- assign pre_toc = pre_toc | split: strip_marker | first -%}
{%- endif -%}

{%- comment -%} Normalize README's inline "Back to top" blocks. {%- endcomment -%}
{%- capture back_orig -%}<div align="right"><a href="#site-top">↑ Back to top</a></div>{%- endcapture -%}
{%- capture back_classed -%}<div class="car-backlink" align="right"><a href="#site-top">↑ Back to top</a></div>{%- endcapture -%}
{%- assign car_html = pre_toc | replace: back_orig, back_classed -%}

{{ car_html | markdownify }}

<!-- Mobile/compact-only: Back to top BETWEEN Summary and About -->
<div class="backlink--injected" align="right"><a href="#site-top">↑ Back to top</a></div>
<hr class="m-divider" />

<!-- ===== Mobile-only Author Card injected AFTER the story section ===== -->
<div class="author-card author-card--mobile">
  <div class="author-card__heading">About the Author</div>

  <a href="{{ site.author_photo }}" target="_blank" rel="noopener">
    <img class="author-card__photo" src="{{ site.author_photo }}" alt="{{ site.author }}">
  </a>

  <div class="author-card__name">{{ site.author }}</div>
  {% if site.author_title %}<div class="author-card__title"><em>{{ site.author_title }}</em></div>{% endif %}
  {% if site.author_summary %}<p class="author-card__summary">{{ site.author_summary }}</p>{% endif %}

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

{% if post_toc %}
  {% capture rest %}## Table of Contents{{ post_toc }}{% endcapture %}
  {{ rest | markdownify }}
{% endif %}
 
