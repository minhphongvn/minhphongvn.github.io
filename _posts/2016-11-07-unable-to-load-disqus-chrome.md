---
layout: post
title: "Unable to load Disqus on Google Chrome"
menutitle: "Unable to load Disqus on Google Chrome"
date: 2016-11-07 15:23:00 +0000
tags: unable load Disqus Chrome
category: Website
author: am
published: true
redirect_from: "/2016-11-07-unable-to-load-disqus-chrome/"
language: EN
comments: true
---

I had the following error with Disqus comments on Google Chrome 

<figure>
  <img src="{{ site.baseurl }}/media{{page.redirect_from}}unable-to-load-disqus.png" />
  <figcaption>We were unable to load Disqus. If you are a moderator please see our <a href="https://help.disqus.com/customer/portal/articles/472007-i-m-receiving-the-message-%22we-were-unable-to-load-disqus-%22">troubleshooting guide</a>.</figcaption>
</figure>

This was solved by turning off all extensions and turning them back on one at a time.

The offender was [TeX All the Things][2] and comments were available again with it disabled. 
[This Reddit Post][3] also indicates that Chrome extensions can often cause issues for the 
comments box.
 
# References
 - [Disqus Docs: I'm receiving the message...][1]
 - [TeX All the Things][2]
 - [Reddit: Chrome & Disqus not playing nice...any suggestions][3]
 
 [1]: https://help.disqus.com/customer/portal/articles/472007-i-m-receiving-the-message-%22we-were-unable-to-load-disqus-%22
 [2]: https://github.com/emichael/texthings/issues/16
 [3]: https://www.reddit.com/r/chrome/comments/167h36/chrome_disqus_not_playing_niceany_suggestions/