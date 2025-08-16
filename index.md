---
layout: default
title: Data-Backed Decision Making for YouTube Campaigns
---

{% comment %}
Capture README, convert to HTML, then rewrite relative src/href that start
with "images/" or "data/" to include the site.baseurl so they work on
project pages. This keeps README clean for GitHub while fixing links on Pages.
{% endcomment %}

{% capture readme_raw %}{% include_relative README.md %}{% endcapture %}
{% assign html = readme_raw | markdownify %}

{% assign img_src_prefix   = 'src="'  | append: site.baseurl | append: '/images/' %}
{% assign img_href_prefix  = 'href="' | append: site.baseurl | append: '/images/' %}
{% assign data_href_prefix = 'href="' | append: site.baseurl | append: '/data/' %}

{% assign fixed = html
  | replace: 'src="images/',  img_src_prefix
  | replace: 'href="images/', img_href_prefix
  | replace: 'href="data/',   data_href_prefix
%}

<div class="readme-wrap">
{{ fixed }}
</div>
