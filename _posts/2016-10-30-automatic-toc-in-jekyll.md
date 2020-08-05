---
layout:            post
title:             "Automatic Table of Contents for Jekyll Blogs"
menutitle:         "Automatic Table of Contents for Jekyll Blogs"
date:              2016-10-30 16:58:00 +0000
tags:              Automatic Table of Contents Jekyll Blogs
category:          Website
author:            am
published:         true
redirect_from:     "/2016-10-30-automatic-toc-in-jekyll/"
language:          EN
comments:          true
---

Download the source code for this page [here][2]

# Contents
{:.no_toc}

* This will become a table of contents (this text will be scraped).
{:toc}

# Introduction
This is more of a personal bookmark so I don't forget this super simple solution

# Method
Include the following in the `_config.yml` file

    markdown: kramdown

then add this line where you want the TOC to appear in the markdown blog entry

    * This will become a table of contents (this text will be scraped).
    {:toc}

This will also include `Contents` inside TOC which looks dumb.

Correct this by `{:.no_toc}` following a title you don't want in the TOC. 

# References
 - [`kramdown` docs][1]
 - [Source Code][2]

[1]: http://kramdown.gettalong.org/converter/html.html
[2]: https://github.com/flipdazed/flipdazed.github.io/blob/master/_posts/2016-10-30-automatic-toc-in-jekyll.md