---
layout: default
title: Data-Backed Decision Making for YouTube Campaigns
---

{% comment %}
1) Pull README
2) Convert to HTML
3) Prefix relative links (images/, data/, docs/, scripts/, visualizations/) with site.baseurl
   so they work on project pages.
{% endcomment %}

{% capture readme_raw %}{% include_relative README.md %}{% endcapture %}
{% assign html = readme_raw | markdownify %}

{% assign p_img_src_abs  = 'src="'  | append: site.baseurl | append: '/images/' %}
{% assign p_img_href_abs = 'href="' | append: site.baseurl | append: '/images/' %}
{% assign p_data_abs     = 'href="' | append: site.baseurl | append: '/data/' %}
{% assign p_docs_abs     = 'href="' | append: site.baseurl | append: '/docs/' %}
{% assign p_scripts_abs  = 'href="' | append: site.baseurl | append: '/scripts/' %}
{% assign p_viz_abs      = 'href="' | append: site.baseurl | append: '/visualizations/' %}

{% assign fixed = html
  | replace: 'src="/images/',  p_img_src_abs
  | replace: 'src="images/',   p_img_src_abs
  | replace: 'href="/images/', p_img_href_abs
  | replace: 'href="images/',  p_img_href_abs
  | replace: 'href="/data/',   p_data_abs
  | replace: 'href="data/',    p_data_abs
  | replace: 'href="/docs/',   p_docs_abs
  | replace: 'href="docs/',    p_docs_abs
  | replace: 'href="/scripts/', p_scripts_abs
  | replace: 'href="scripts/',  p_scripts_abs
  | replace: 'href="/visualizations/', p_viz_abs
  | replace: 'href="visualizations/',  p_viz_abs
%}

<div class="readme-wrap">
{{ fixed }}
</div>
