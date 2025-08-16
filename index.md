---
layout: default
title: Data-Backed Decision Making for YouTube Campaigns
---

{% comment %}
Render README.md as HTML. Because the page lives at /<baseurl>/,
all relative links like images/... and data/... will resolve correctly.
{% endcomment %}

{% capture readme_raw %}{% include_relative README.md %}{% endcapture %}
<div class="readme-wrap">
{{ readme_raw | markdownify }}
</div>
