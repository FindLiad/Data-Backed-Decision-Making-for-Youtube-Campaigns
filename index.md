---
layout: default
title: Project 1 | YouTube Campaign Analytics
---

{% comment %}
Render README starting at the CAR section, then inject:
  (mobile only) Back to top BETWEEN Summary and About,
  a faint divider,
  the mobile About card,
  (mobile only) Back to top AFTER About,
  then the Table of Contents.
On desktop: show only the README’s own inline Back-to-top (classed), and NO mobile About card.
All “Back to top” links target #site-top (beige banner at absolute top).
{% endcomment %}

{% capture readme_raw %}{% include_relative README.md %}{% endcapture %}

{% assign token1 = '## A time I went above and beyond to deliver for the customer' %}
{% assign token2 = '## Summary' %}
{% assign start_token = token2 %}
{% if readme_raw contains token1 %}{% assign start_token = token1 %}{% endif %}

{% assign after_start = readme_raw | split: start_token %}
{% if after_start.size > 1 %}
  {% capture from_car %}{{ start_token }}{{ after_start[1] }}{% endcapture %}
{% else %}
  {% assign from_car = readme_raw %}
{% endif %}

{% assign toc_split = from_car | split: '## Table of Contents' %}
{% assign car_part = toc_split[0] %}
{% assign toc_part = toc_split[1] %}

{%- capture back_orig -%}<div align="right"><a href="#site-top">↑ Back to top</a></div>{%- endcapture -%}
{%- capture back_classed -%}<div class="car-backlink" align="right"><a href="#site-top">↑ Back to top</a></div>{%- endcapture -%}
{% assign car_html = car_part | replace: back_orig, back_classed %}

{{ car_html | markdownify }}

<!-- MOBILE/COMPACT ONLY: Back to top between Summary and About, divider, About card, then another Back to top -->
<div class="backlink--injected" align="right"><a href="#site-top">↑ Back to top</a></div>
<hr class="m-divider" />

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

{% if toc_part %}
  {% capture rest %}## Table of Contents{{ toc_part }}{% endcapture %}
  {{ rest | markdownify }}
{% endif %}

