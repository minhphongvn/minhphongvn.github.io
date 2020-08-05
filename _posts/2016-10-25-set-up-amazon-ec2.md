---
layout: post
title: "Set Up Amazon Elastic Compute Cloud (EC2)"
menutitle: "Set Up Amazon Elastic Compute Cloud (EC2)"
date: 2016-10-25 16:31:00 +0100
tags: Amazon Web Services Cloud EC2
category: Deep Learning
author: am
published: true
redirect_from: "/2016-10-25-set-up-amazon-ec2/"
language: EN
comments: true
---

This is the first part of a multi-part guide on GPU cloud computing for Deep Learning

1. [Set Up Amazon Elastic Compute Cloud (EC2)]({% post_url 2016-10-25-set-up-amazon-ec2 %})
2. [Theano on Amazon Web Services for Deep Learning]({%post_url 2016-10-25-theano-on-amazon-web-services-for-deep-learning %})
3. [Set up Microsoft Azure for CUDA Cloud]({% post_url 2016-10-29-set-up-microsoft-azure %})

This guide more generally demonstrates how to register for  Amazon Web Services and 
set up the Amazon Elastic Compute Cloud (EC2).

# Contents
 1. [Requirements](#reqs)
 2. [Register for AWS](#register)
 3. [Create an Amazon Machine Instance (AMI) on EC2](#create)
 4. [Launch and Connect with SSH](#launch)
 5. [Close instance](#close)
 6. [Usage Plans for GPU Compute Instances](#usage)
 7. [Alternative Elastic Clouds with CUDA](#alt)
 
<a id="reqs"></a>

# Requirements

 - A Linux OS. I have a Macbook
 - A credit / debit card
 - A phone number you are willing to use

<a id="register"></a>

# Registering for Amazon Web Services

- Visit [AWS][1] and **Create a Free Account**

The process is straightforward and the usual series of personal details (you **need** to use a 
real phone number), email verifications and captcha images to fill out. 
I registered a *Personal Account*. You will also be asked to submit card details as this is a
 paid service. You will then be asked to receive a call from AWS to verify a PIN. This call occurs 
 immediately after requesting. I then chose the *Basic* support plan on the premise that it 
 would be easier to upgrade than downgrade. You will then receive an email within a few 
 seconds confirming the account is ready. You can then Sign In again.

### Free Tier
Half way through writing this guide I received a nice email stating

> Thank you for creating an Amazon Web Services (AWS) account. 
> For the next 12 months, you will have free access to compute, storage, database, 
> and application services. Learn more by visiting our [Free Tier][4] page.

The GPU computing instances are not free unfortunately. However, a Free Tier instance is
a good way of familiarising with launch and connection to EC2.

<a id="create"></a>

# Create an Amazon Machine Instance
 - These images show how to set up an Instance
 - The Free Tier will be used for this example but GPU Compute should be used in production

## Set Region

<div class="album">
   <figure>
      <img src="{{ site.baseurl }}/media{{page.redirect_from}}Navigate-to-EC2.png" />
      <figcaption>Navigate to the EC2 landing page</figcaption>
   </figure>
   <figure>
      <img src="{{ site.baseurl }}/media{{page.redirect_from}}select-region.png" />
      <figcaption>Select Region in the top right</figcaption>
   </figure>
</div>

<a id="key-value"></a>

## Create Key-Value Pair
This will save some effort later. Create a key-value pair and make sure to save the `.pem` file
securely after doing so.
<div class="album">
    <figure>
        <img src="{{ site.baseurl }}/media{{page.redirect_from}}key-value-pair.png" />
        <figcaption>Navigate to the Key Pairs in menu on the left
        </figcaption>
    </figure>
    <figure>
        <img src="{{ site.baseurl }}/media{{page.redirect_from}}create-key-value-pair.png" />
        <figcaption>Download the .pem file to ~/Downloads</figcaption>
    </figure>
</div>
<a id="key-value-storing"></a>

## Storing the Key Properly

It is [advisable][6] to store the key with the following set of commands

<pre class="line-numbers language-bash"><code>#set filename
filename=pem_filename.pem
# create a root directory for SSH
mkdir ~/.ssh
# sometimes the files come from amazon as ".pem.txt"
mv ~/Downloads/${filename}* ~/.ssh/${filename}
    
# change permissions so only root can read the file
chmod 400 ~/.ssh/${filename}
{
    echo "Host *amazonaws.com"
    echo "IdentityFile ~/.ssh/${filename}"
    echo "User ubuntu" 
} > ~/.ssh/config</code></pre>

## Create AMI

<div class="album">
   <figure>
      <img src="{{ site.baseurl }}/media{{page.redirect_from}}Launch-instance-from-EC2-Home-Page.png" />
      <figcaption>Launch an Instance</figcaption>
   </figure>
   <figure>
      <img src="{{ site.baseurl }}/media{{page.redirect_from}}Choose-AMI.png" />
      <figcaption>Choose Ubuntu AMI  (ami-d732f0b7)</figcaption>
   </figure>
   <figure>
      <img src="{{ site.baseurl }}/media{{page.redirect_from}}Choose-instance-type.png" />
      <figcaption>Choose GPU Compute Instance</figcaption>
   </figure>
</div>

Astute observers will notice I have *Oregon* in some of the screenshots instead of *Ireland*. 
That is because I forgot to change my region in my first attempt!

## Other Settings
 - A few more settings are required

<div class="album">
   <figure>
      <img src="{{ site.baseurl }}/media{{page.redirect_from}}Choose-storage.png" />
      <figcaption>Choose storage</figcaption>
   </figure>
   <figure>
      <img src="{{ site.baseurl }}/media{{page.redirect_from}}Tag-Spot-Request.png" />
      <figcaption>I don't think this matters much</figcaption>
   </figure>
   <figure>
      <img src="{{ site.baseurl }}/media{{page.redirect_from}}Security-group.png" />
      <figcaption>Recommend changing Source from Anywhere to My IP</figcaption>
   </figure>
   <figure>
      <img src="{{ site.baseurl }}/media{{page.redirect_from}}Review.png" />
      <figcaption>Unfortunately GPU Compute Instances are not free</figcaption>
   </figure>
</div>

At this point I would recommend not selecting a GPU instance and instead changing it
to a **Free Tier** Instance. This will be how I continue the guide.

<a id="launch"></a>

# Launch and Connect with SSH
 - Launching an instance will start the billing process
 
 The SSH process is very simple if the steps for [Storing the Key Properly](#key-value-storing)
 were followed

<div class="album">
   <figure>
      <img src="{{ site.baseurl }}/media{{page.redirect_from}}start-instances.png" />
      <figcaption>Request Spot Instance and View Spot Requests</figcaption>
   </figure>
   <figure>
      <img src="{{ site.baseurl }}/media{{page.redirect_from}}view-instances.png" />
      <figcaption>Right-click connect for connection instructions</figcaption>
   </figure>
   <figure>
     <img src="{{ site.baseurl }}/media{{page.redirect_from}}connect-with-ssh.png" />
     <figcaption>The process is simpler than this!</figcaption>
   </figure>
</div>

You can then SSH into the Instance simply with the command

<pre class="line-numbers language-bash"><code>ssh ubuntu@[DNS]</code></pre>

The correct DNS will be different for each Instance. Obtain this information by 

 -  right-clicking the instance in the dashboard and selecting *connect* 
 - or selecting the Instance and viewing the Description below

<figure>
 <img src="{{ site.baseurl }}/media{{page.redirect_from}}ssh-connect.png" />
 <figcaption>Inside the Amazon EC2 Instance! Check the documentation][5] to 
     ensure this is up to date if you have issues</figcaption>
</figure>

<a id="close" />

# Close Instance

Make sure that you check the instance has been closed **in addition** to the Spot request! I 
received a 31 hour bill for an unclosed GPU Compute instance that I had thought I closed
 which was rather annoying.

<figure>
  <img src="{{ site.baseurl }}/media{{page.redirect_from}}Cancel-request.png" />
  <figcaption>Cancel request</figcaption>
</figure>

<a id="usage" />

# Usage Plans for GPU Compute Instances

 - I selected a [Spot Instance][2] with a maximum bid of $0.10 / hour
 - [Persistent Requests][3] will be resubmitted every time your Spot Instance is terminated
 
<figure>
   <img src="{{ site.baseurl }}/media{{page.redirect_from}}Configure-Instance.png" />
   <figcaption>Spot Instances at up to 90% cheaper but your instance may be terminated.
   More information about Spot Instances can be found 
   <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html?icmpid=docs_ec2_console">here</a>
</figcaption>
</figure>

This excellent graphic from the [AWS docs][2] demonstrates the basic idea of a Spot Instance
<figure>
   <img src="{{ site.baseurl }}/media{{page.redirect_from}}spot_lifecycle.png" />
</figure>

When in production and selecting a Spot payment method, it may be that the spot is higher than
your current maximum bid. If this happens, the Instance will start only when the Spot falls into 
range. It's sensible to look at price history if you wish to minimise interruptions.

<figure>
  <img src="{{ site.baseurl }}/media{{page.redirect_from}}gpu-instance-status.png" />
  <figcaption>An example of a paid instance with a spot higher than the max bid</figcaption>
</figure>

# Using EC2 for Deep Learning
See Part 2 for setting up
[Theano on Amazon Web Services for Deep Learning]({%post_url 2016-10-25-theano-on-amazon-web-services-for-deep-learning %})

<a id="alt" />

# Alternatives

There are [alternative offerings][7] to Amazon EC2.

Out of these the only standout is [Microsoft Azure][8] which is discussed in a 
[following blog]({% post_url 2016-10-29-set-up-microsoft-azure %})

<a id="refs" />

# References
 - [Amazon Web Services][1]
 - [AWS Guide: Using Spot Instances][2]
 - [AWS Guide: Spot Instance Requests][3]
 - [AWS Guide: Free Tier][4]
 - [AWS Guide: Accessing Linux Instances][5]
 - [StackExchange: How to Connect to Amazon EC2 Remotely Using SSH][6]
 - [Nvidia GPU clouds][7]
 - [Microsoft Azure: GPU enabled Virtual Machines][8]

[1]: https://aws.amazon.com
[2]: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html
[3]: https://docs.aws.amazon.com/console/ec2/launchinstance/instance-details/spot-custom
[4]: https://aws.amazon.com/free/
[5]: http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html
[6]: http://unix.stackexchange.com/a/115860
[7]: http://www.nvidia.com/object/gpu-cloud-computing-services.html
[8]: https://azure.microsoft.com/en-gb/pricing/details/virtual-machines/series/#n-series