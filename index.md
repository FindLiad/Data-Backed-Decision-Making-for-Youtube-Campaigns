---
layout: default
title: Data-Backed Decision Making for YouTube Campaigns
---

{% comment %}
Show README starting at the CAR "Summary" section (or fallback to generic "## Summary"),
then split at "## Table of Contents". We convert the CAR's inline Back-to-top(s) into a
classed element (car-backlink) so CSS can toggle for mobile/desktop.
{% endcomment %}

{% capture readme_raw %}{% include_relative README.md %}{% endcapture %}

{% assign token_car = '## A time I went above and beyond to deliver for the customer' %}
{% assign token_summary = '## Summary' %}

{% if readme_raw contains token_car %}
  {% assign start_token = token_car %}
{% else %}
  {% assign start_token = token_summary %}
{% endif %}

{% assign after_start = readme_raw | split: start_token %}
{% if after_start.size > 1 %}
  {% capture body_from_start %}{{ start_token }}{{ after_start[1] }}{% endcapture %}
{% else %}
  {% assign body_from_start = readme_raw %}
{% endif %}

{% assign toc_split = body_from_start | split: '## Table of Contents' %}

{%- comment -%}
Normalize any inline Back-to-top blocks to .car-backlink and target absolute site top.
Handles both #site-top and (legacy) #table-of-contents variants.
{%- endcomment -%}
{% capture back_orig_site %}<div align="right"><a href="#site-top">↑ Back to top</a></div>{% endcapture %}
{% capture back_orig_toc  %}<div align="right"><a href="#table-of-contents">↑ Back to top</a></div>{% endcapture %}
{% capture back_classed   %}<div class="car-backlink" align="right"><a href="#site-top">↑ Back to top</a></div>{% endcapture %}

{% if toc_split.size > 1 %}
  {% assign pre = toc_split[0] | replace: back_orig_site, back_classed | replace: back_orig_toc, back_classed %}
  {{ pre | markdownify }}

  <!-- Back to top shown only on mobile/compact via CSS -->
  <div class="backlink--injected" align="right">
    <a href="#site-top">↑ Back to top</a>
  </div>

  {% capture rest %}## Table of Contents{{ toc_split[1] }}{% endcapture %}
  {{ rest | markdownify }}
{% else %}
  {% assign pre = body_from_start | replace: back_orig_site, back_classed | replace: back_orig_toc, back_classed %}
  {{ pre | markdownify }}

  <div class="backlink--injected" align="right">
    <a href="#site-top">↑ Back to top</a>
  </div>
{% endif %}
