---
layout:            post
title:             "Optimising a Jekyll Blog for Google"
menutitle:         "Optimising a Jekyll Blog for Google"
date:              2016-09-23 06:31:00 +0100
tags:              Optimising Jekyll Blog Google Search
category:          Website
author:            am
published:         true
redirect_from:     "/optimising-blog-for-google/"
language:          EN
comments:          true
---

<div class="tip">
<b>Time Saver</b>
<br> <a href="https://github.com/flipdazed/flipdazed.github.io">Fork my site</a> and customise it yourself
</div>

# Jekyll Plugins
The following gems will help in particular

```jekyll 
gems:
  - jekyll-sitemap
  - jekyll-seo-tag
```

The first will create a sitemap for a crawler bot with no other effort. The latter requires the following line top be present in the `<head><\head>` section of the site

```jekyll 
{% raw %} {% seo %} {% endraw %}
```
see the [official docs](https://help.github.com/articles/search-engine-optimization-for-github-pages/) for more information

# Google WebMaster Tools
This is the proper way of getting 'crawled' by Google. In fact, Google also provide a lot of helpful tips through this tool to aid your search discovery.

# Alternative without verifying
It is also possible to submit a request for the google crawler to map the site through [this form](https://www.google.com/webmasters/tools/submit-url?pli=1) without any verification procedure. I did both.