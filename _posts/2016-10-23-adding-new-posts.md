---
layout:            post
title:             "Adding a Jekyll Blog Entry"
menutitle:         "Adding a Jekyll Blog Entry"
date:              2016-10-23 06:31:00 +0100
tags:              Adding Jekyll Blog Entry
category:          Website
author:            am
published:         true
redirect_from:     "/adding-new-posts/"
language:          EN
comments:          true
---

This is basically a note-to-self as I do this infrequently and keep forgetting!

# Post Template
This is required at the top of each page

<pre class="line-numbers language-liquid"><code>---
layout:            post
title:             "Adding a Jekyll Blog Entry"
menutitle:         "Adding a Jekyll Blog Entry"
date:              2016-10-23 06:31:00 +0100
tags:              Adding Jekyll Blog Entry
category:          Website
author:            am
published:         true
redirect_from:     "/adding-new-posts/"
language:          EN
comments:          true
---</code></pre>

Setting `published: false` will hide the post from public view. The date determines the order of the posts in the blog. Future dates will not show on the landing page.

# Testing
Navigate to the website directory. I installed ruby through the [Ruby Version Manager (RVM)](https://rvm.io/). I don't think I did it correctly as I need to run the following each time a new terminal is opened
<pre class="language-terminal"><code>rvm get head
bundle install</code></pre>

The website can then be previewed by entering the following in the terminal

<pre class="language-terminal"><code>bundle exec jekyll serve</code></pre>

Commit and Push the changes to finalise.