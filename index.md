---
layout: default
title: Data-Backed Decision Making for YouTube Campaigns
---

{% comment %}
Render README.md so repo and site stay in sync.
Drop the README's first H1 to avoid duplicating the banner title.
This version is robust to leading blank lines/whitespace.
{% endcomment %}

{% capture readme_raw %}{% include_relative README.md %}{% endcapture %}
{% assign readme = readme_raw | replace: "\r\n", "\n" | strip %}
{% assign lines = readme | split: "\n" %}
{% if lines.size > 0 and lines[0] contains '# ' %}
  {% assign trimmed = lines | slice: 1, lines.size | join: "\n" %}
  {{ trimmed | markdownify }}
{% else %}
  {{ readme | markdownify }}
{% endif %}
