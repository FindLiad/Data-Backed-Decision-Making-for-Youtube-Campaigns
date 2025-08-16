---
layout: default
title: Data-Backed Decision Making for YouTube Campaigns
---

{% comment %}
Render README.md but drop everything before the first "## Summary".
{% endcomment %}

{% capture readme_raw %}{% include_relative README.md %}{% endcapture %}
{% assign split_token = '## Summary' %}
{% assign parts = readme_raw | split: split_token %}
{% if parts.size > 1 %}
  {% capture after %}{{ split_token }}{{ parts[1] }}{% endcapture %}
  {{ after | markdownify }}
{% else %}
  {{ readme_raw | markdownify }}
{% endif %}
