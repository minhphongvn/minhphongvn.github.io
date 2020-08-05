---
layout: post
title: "Adding a Video to a GitHub Readme (and Jekyll Blogs)"
menutitle: "Adding a Video to a GitHub Readme (and Jekyll Blogs)"
date: 2016-10-24 22:31:00 +0100
tags: Adding Video GitHub Readme
category: Website
author: am
published: true
redirect_from: "/2016-10-24-add-video-to-github-README/"
language: EN
comments: true
---

<figure>
   <img src="{{ site.baseurl }}/media{{page.redirect_from}}visualise_params.gif"/>
   <figcaption>The cost is negative of what is should be but I reversed it in the SGD algorithm so it doesn't matter</figcaption>
</figure>

Basic instructions on how to use `ffmpeg` to embed a user friendly video from a series of
plots into a `README.md` in GitHub.

# Requirements
  - Mac user (can use `apt-get` on Linux for installs)
  - [`convert`](http://www.imagemagick.org/script/convert.php)
 
Get `convert` with [`homebrew`](http://brew.sh/) as

    brew install imagemagick

# Creating an Animation

    convert -delay 10 -loop 0 input*.png output.gif

 - `-delay 10` means `10*10ms`so a delay of a `-delay 100` is `1s`
 - `-loop 0` states there is no pause before looping
 
 If you find your `.gif` is too large then the size can be **significantly reduced** with
 
     convert input.gif \
         -fuzz 10% -layers Optimize \
         output.gif

In my example this reduced the size from a whopping `147MB` to `3MB`!

# Dynamic Movie format for Jekyll Sites
This won't work for Github README files but it is worth stating anyway for Jekyll based sites 
that use markdown.

<figure class="large">
    <div class="myvideo">
       <video  style="display:block; width:100%; height:auto;" autoplay controls loop="loop">
           <source src="{{ site.baseurl }}/media{{page.redirect_from}}visualise_params.mp4" type="video/mp4" />
           <source src="{{ site.baseurl }}/media{{page.redirect_from}}visualise_params.ogv" type="video/ogg" />
           <source src="{{ site.baseurl }}/media{{page.redirect_from}}visualise_params.webm"  type="video/webm"  />
       </video>
    </div>
<figcaption>A nice movie format</figcaption>
</figure>

## Requirements

 - [`ffmpeg`](https://www.ffmpeg.org/)

Get `ffmpeg` with

     brew install ffmpeg --with-libvpx

 if you obtain an error of [`Unknown encoder 'libvpx'`](http://stackoverflow.com/q/11003420/4013571)  
 or [`Unknown encoder 'libtheora'`]() then  you need to do

     brew reinstall ffmpeg --with-libvpx --with-theora --with-libvorbis

## Movie from Plots
I assume that images are outputted by a plotting software such as `gnuplot` of `mathplotlib`
at regular intervals. They should be numbered sequentially.

    ffmpeg -r 60 -f image2 -s 1920x1080 \
        -pattern_type glob -i 'input*' \
        -vcodec libx264 -crf 25  -pix_fmt yuv420p \
        output.mp4

 - `-r 60` this sets the framerate to `60fps`
 - `-pattern_type glob -i 'input*'` matches all files with `input` and reads in order
 - `output.mp4` output file name
 - `-s 1920x1080` set the output resolution

## Dynamically resize
Some browsers don't recognise `.mp4` files forcing the use of a Flash plugin. This format 
allows `HTML5` to use its default plugin

    ffmpeg -i input.mp4 \
        -vcodec libvpx -acodec libvorbis \
        output.webm

The following format is also necessary for [multi-browser support](http://stackoverflow.com/a/11188058/4013571)

    ffmpeg -i visualise_params.mp4 \
        -c:v libtheora -c:a libvorbis -q:v 10 -q:a 10 \
        visualise_params.ogv

## Adding the CSS
Add the `css` code to `_sass/call_me_what_you_like.scss`

<pre class="line-numbers language-css"><code>// Adds support for a video holder
// as per http://webdesignerwall.com/tutorials/css-elastic-videos

.myvideo {
position : relative;
display : block;
width : 30%;
min-width : 200px;
margin : auto;
height : auto;
}
.flex-video {
position : relative;
padding-bottom : 67.5%;
height : 0;
overflow : hidden;
}
.flex-video iframe, .flex-video object, .flex-video embed {
position : absolute;
top : 0;
left : 0;
width : 100%;
height : 100%;
}
</code></pre>

## Adding the HTML
The following HTML will then generate the correct video in your Jekyll site. 

<pre class="line-numbers language-html"><code>&lt;div class="myvideo"&gt;
   &lt;video  style="display:block; width:100%; height:auto;" autoplay controls loop="loop"&gt;
       &lt;source src="{% raw %}{{ site.baseurl }}{% endraw %}/media{{page.redirect_from}}visualise_params.mp4" type="video/mp4" /&gt;
       &lt;source src="{% raw %}{{ site.baseurl }}{% endraw %}/media{{page.redirect_from}}visualise_params.ogv" type="video/ogg" /&gt;
       &lt;source src="{% raw %}{{ site.baseurl }}{% endraw %}/media{{page.redirect_from}}visualise_params.webm"  type="video/webm"  /&gt;
   &lt;/video&gt;
&lt;/div&gt;</code></pre>

In this actual case I also wrapped the `<div>` tag within a `<figure>` tag that is provided in this
site's template

<pre class="line-numbers language-html"><code>&lt;figure class="large"&gt;
    &lt;div class="myvideo"&gt;
       &lt;video  style="display:block; width:100%; height:auto;" autoplay controls loop="loop"&gt;
           &lt;source src="{{ site.baseurl }}/media{{page.redirect_from}}visualise_params.mp4" type="video/mp4" /&gt;
           &lt;source src="{{ site.baseurl }}/media{{page.redirect_from}}visualise_params.ogv" type="video/ogg" /&gt;
           &lt;source src="{{ site.baseurl }}/media{{page.redirect_from}}visualise_params.webm"  type="video/webm"  /&gt;
       &lt;/video&gt;
    &lt;/div&gt;
&lt;figcaption&gt;A nice movie format&lt;/figcaption&gt;
&lt;/figure&gt;</code></pre>

# References

 - [Embedding video in GitHub](https://github.com/etianen/html5media/wiki/embedding-video)
 - [WebM web video encoding tutorial with FFMpeg](https://www.virag.si/2012/01/webm-web-video-encoding-tutorial-with-ffmpeg-0-9/)
 - [Unknown Error with `'libvpx'`](http://stackoverflow.com/q/11003420/4013571)
 - [Do I need both WebM and ogv formats when using HTML5 video?](http://stackoverflow.com/q/11187316/4013571)
 - [CSS Elastic Videos](http://webdesignerwall.com/tutorials/css-elastic-videos)