---
layout: post
title: "Set up Microsoft Azure for CUDA Cloud"
menutitle: "Set up Microsoft Azure for CUDA Cloud"
date: 2016-10-25 03:02:00 +0100
tags: Microsoft Azure GPU CUDA Cloud
category: Deep Learning
author: am
published: true
redirect_from: "/2016-10-29-set-up-microsoft-azure/"
language: EN
comments: true
---

This is the third part of a multi-part guide on GPU cloud computing for Deep Learning

1. [Set Up Amazon Elastic Compute Cloud (EC2)]({% post_url 2016-10-25-set-up-amazon-ec2 %})
2. [Theano on Amazon Web Services for Deep Learning]({%post_url 2016-10-25-theano-on-amazon-web-services-for-deep-learning %})
3. [Set up Microsoft Azure for CUDA Cloud]({% post_url 2016-10-29-set-up-microsoft-azure %})

This guide more generally demonstrates how to register for Microsoft Azure and set up a cloud
instance.

**At the time of writing, Microsoft the Virtual Machine Instances with NVIDIA GPUs
 are not yet publicly available. However, it is possible to register for preview access [HERE][9]**
 
 In the meantime I provide brief links and instructions on registering for Microsoft Azure services.


# Contents
 1. [Requirements](#reqs)
 2. [Registering for Microsoft Azure](#register)
 3. [Alternative](#alt)
 4. [References](#refs)
 
<a id="reqs"></a>

# Requirements

 - A Linux OS. I have a Macbook
 - A Microsoft Live Account
 - A credit / debit card
 - A phone number you are willing to use

<a id="register"></a>

# Registering for Microsoft Azure

 - Register for Microsoft Azure [here][1]
 
 The process is very similar to Amazon EC2 with personal details (again, you **need** to use a 
real phone number) and email verifications. This will then take you to the default set up page.

I will update with more details with GPU Compute is released.

<a id="alt" />

# Alternatives

There are [alternative offerings][7] to Microsoft Azure.

Out of these the only other viable option is [Amazon EC2][8] which is discussed in a 
[previous blog entry]({% post_url 2016-10-25-set-up-amazon-ec2 %})

<a id="refs" />

# References
 - [Register for Microsoft Azure][1]
 - [Microsoft Azure: GPU enabled Virtual Machines][2]
 - [Nvidia GPU clouds][7]
 - [Amazon Web Services][8]

[1]: https://azure.microsoft.com/en-gb/free/
[2]: https://azure.microsoft.com/en-gb/pricing/details/virtual-machines/series/#n-series
[7]: http://www.nvidia.com/object/gpu-cloud-computing-services.html
[8]: https://aws.amazon.com
[9]: https://azure.microsoft.com/en-gb/blog/azure-n-series-preview-availability/