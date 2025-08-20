---
layout: default
title: Data-Backed Decision Making for YouTube Campaigns
---

{% comment %}
Prefer our CAR summary section; otherwise fall back to other known headings.
{% endcomment %}

{% capture readme_raw %}{% include_relative README.md %}{% endcapture %}
{% assign keys = '## A time I went above and beyond to deliver for the customer|## Business Requirements vs. Customer Needs|## Summary' | split: '|' %}
{% assign picked = '' %}
{% for k in keys %}
  {% assign parts = readme_raw | split: k %}
  {% if parts.size > 1 and picked == '' %}
    {% assign picked = k %}
    {% capture after %}{{ k }}{{ parts[1] }}{% endcapture %}
  {% endif %}
{% endfor %}

{% if picked != '' %}
  {{ after | markdownify }}
{% else %}
  {{ readme_raw | markdownify }}
{% endif %}
