---
layout: default
title: Data-Backed Decision Making for YouTube Campaigns
---

{% comment %}
Capture README, convert to HTML with markdownify, then wrap for styling.
This avoids the "raw markdown showing" issue you saw.
{% endcomment %}

{% capture readme_raw %}{% include_relative README.md %}{% endcapture %}
<div class="readme-wrap">
{{ readme_raw | markdownify }}
</div>
