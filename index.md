---
layout: default
title: Data-Backed Decision Making for YouTube Campaigns
---

{% comment %}
This pulls README.md into the site so README is the single source of truth.
The first H1 (# ...) is dropped to avoid duplicating the banner title.
{% endcomment %}

{% capture readme %}{% include_relative README.md %}{% endcapture %}
{% assign lines = readme | split: "\n" %}
{% if lines.first contains '# ' %}
  {% assign trimmed = lines | slice: 1, lines.size | join: "\n" %}
  {{ trimmed | markdownify }}
{% else %}
  {{ readme | markdownify }}
{% endif %}
