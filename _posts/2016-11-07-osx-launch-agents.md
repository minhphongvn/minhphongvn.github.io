---
layout: post
title: "Removing Broken OSX Launch Daemons: net.juniper.AccessService"
menutitle: "Removing Broken OSX Launch Daemons"
date: 2016-11-07 15:23:00 +0000
tags: OSX LaunchDaemons net.juniper.AccessService
category: OSX Maintenance
author: am
published: true
redirect_from: "/2016-11-07-osx-launch-agents.md/"
language: EN
comments: true
---

Start the console

<pre class="language-bash"><code>open /Applications/Utilities/Console.app</code></pre>

Look at `system.log` reports. This can also be viewed by

<pre class="language-bash"><code>syslog -w</code></pre>

My mac has a launch daemon running repeatedly in the background every `10s`


<pre class="language-terminal"><code>Nov  7 15:32:15 iBanterMacBook com.apple.xpc.launchd[1] (net.juniper.AccessService[3276]): Service could not initialize: Unable to set current working directory. error = 2: No such file or directory, path = /Applications/Junos Pulse.app/Contents/Plugins/JUNS: 16B2555: xpcproxy + 11207 [1356][4A173B59-A786-3CBF-9740-CFC693060FEF]: 0x2
Nov  7 15:32:15 iBanterMacBook com.apple.xpc.launchd[1] (net.juniper.AccessService): Service only ran for 0 seconds. Pushing respawn out by 10 seconds.
Nov  7 15:32:25 iBanterMacBook com.apple.xpc.launchd[1] (net.juniper.AccessService[3277]): Service could not initialize: Unable to set current working directory. error = 2: No such file or directory, path = /Applications/Junos Pulse.app/Contents/Plugins/JUNS: 16B2555: xpcproxy + 11207 [1356][4A173B59-A786-3CBF-9740-CFC693060FEF]: 0x2
Nov  7 15:32:25 iBanterMacBook com.apple.xpc.launchd[1] (net.juniper.AccessService): Service only ran for 0 seconds. Pushing respawn out by 10 seconds.
</code></pre>

I has uninstalled this program months previously. I finding the relevant  launch daemon by

<pre class="language-bash"><code>grep -lR juniper /System/Library/Launch* /Library/Launch* ~/Library/LaunchAgents/</code></pre>

where `grep -lR juniper` will search for all files in the following directories 
containing the pattern `juniper`

In this case the offenders were located at

    /Library/LaunchDaemons/net.juniper.AccessService.plist
    /Library/LaunchDaemons/net.juniper.UninstallPulse.plist
    /Library/LaunchAgents/net.juniper.pulsetray.plist

I can then remove then by

<pre class="line-numbers language-bash"><code>GREP_NAME=juniper
for i in $(grep -lR $GREP_NAME /System/Library/Launch* /Library/Launch* ~/Library/LaunchAgents/);
    do sudo launchctl unload $i
    echo 'unloaded: ' $i
    sudo rm $i
    echo 'removed: '$i
done</code></pre>

you can check the launch daemons by invoking 

<pre class="language-bash"><code>sudo launchctl list | grep $GREP_NAME</code></pre>

If it still remains restart the system. Mine remained as I did not first `unload` the processes
while writing.  Restarting restarted `launchd` properly.