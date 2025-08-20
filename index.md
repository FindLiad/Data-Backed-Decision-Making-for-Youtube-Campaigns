---
layout: default
title: Data-Backed Decision Making for YouTube Campaigns
---

{% comment %}
Render README.md but prefer the “Business Requirements vs. Customer Needs” section
if present; otherwise fall back to “## Summary”.
{% endcomment %}

{% capture readme_raw %}{% include_relative README.md %}{% endcapture %}
{% assign split_token = '## Business Requirements vs. Customer Needs' %}
{% assign parts = readme_raw | split: split_token %}
{% if parts.size > 1 %}
  {% capture after %}{{ split_token }}{{ parts[1] }}{% endcapture %}
  {{ after | markdownify }}
{% else %}
  {% assign split_token2 = '## Summary' %}
  {% assign parts2 = readme_raw | split: split_token2 %}
  {% if parts2.size > 1 %}
    {% capture after2 %}{{ split_token2 }}{{ parts2[1] }}{% endcapture %}
    {{ after2 | markdownify }}
  {% else %}
    {{ readme_raw | markdownify }}
  {% endif %}
{% endif %}
