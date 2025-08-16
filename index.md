---
layout: default
title: Data-Backed Decision Making for YouTube Campaigns
---

{% comment %}
Render README.md so repo and site stay in sync.
Drop the README's first H1 to avoid duplicating the banner title.
{% endcomment %}

{% capture readme %}{% include_relative README.md %}{% endcapture %}
{% assign lines = readme | split: "\n" %}
{% if lines.first contains '# ' %}
  {% assign trimmed = lines | slice: 1, lines.size | join: "\n" %}
  {{ trimmed | markdownify }}
{% else %}
  {{ readme | markdownify }}
{% endif %}
