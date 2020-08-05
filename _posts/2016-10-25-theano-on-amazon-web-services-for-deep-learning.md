---
layout: post
title: "Theano on Amazon Web Services for Deep Learning"
menutitle: "Theano on Amazon Web Services (EC2) for Deep Learning"
date: 2016-10-25 22:31:00 +0100
tags: Theano Amazon Web Services Deep Learning
category: Deep Learning
author: am
published: true
redirect_from: "/2016-10-25-theano-on-amazon-web-services-for-deep-learning/"
language: EN
comments: true
---

This is the second part of a multi-part guide on GPU cloud computing for Deep Learning

1. [Set Up Amazon Elastic Compute Cloud (EC2)]({% post_url 2016-10-25-set-up-amazon-ec2 %})
2. [Theano on Amazon Web Services for Deep Learning]({%post_url 2016-10-25-theano-on-amazon-web-services-for-deep-learning %})
3. [Set up Microsoft Azure for CUDA Cloud]({% post_url 2016-10-29-set-up-microsoft-azure %})

This entry demonstrates how you can offload computational tasks to an Amazon Elastic 
Compute Cloud (EC2) instance through [Amazon Web Services (AWS)][1]. The guide focuses on
 CUDA support for [`Theano`][2].

# Requirements

 - Can set up an EC2 Instance - [see part one]({% post_url 2016-10-25-theano-on-amazon-web-services-for-deep-learning %})
 - Familiarity with Linux and Bash e.g. `sudo`, `wget`, `export`
 - Familiarity with [Ubuntu][3] for `apt-get`

# Contents
 1. [Connect](#connect)
 2. [Load Software](#load)
 3. [Run Code](#run)
 4. [Close Instance](#close)
 5. [Common Errors](#errors)
 6. [References](#refs)

<a id="connect"></a>

# Connect

Connect to the Instance through SSH. Assuming you followed part 1 this is just
<pre class="line-numbers language-bash"><code>ssh ubuntu@[DNS]</code></pre>

<a id="load"></a>

# Load Software
See the references for the sources of these instructions. This code is almost identical with a few 
tweaks.

**Note** you will have to do this each time you start a new Instance

You can download this code as [`install.sh`](({{ site.baseurl }}/media{{page.redirect_from}}/install.sh))
<pre class="line-numbers language-bash"><code># update software
sudo apt-get update
sudo apt-get -y dist-upgrade

# install dependencies
sudo apt-get install -y gcc g++ gfortran build-essential \
    git wget linux-image-generic libopenblas-dev \
    python-dev python-pip ipython python-nose\
    python-numpy python-scipy\
    linux-image-extra-virtual\
    gnuplot-qt # a lot quicker than matplotlib for runtime plots

# install bleeding edge theano
sudo pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git

# get CUDA
sudo wget http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1404/x86_64/cuda-repo-ubuntu1404_7.0-28_amd64.deb

# depackage and install CUDA
sudo dpkg -i cuda-repo-ubuntu1404_7.0-28_amd64.deb
sudo apt-get update
sudo apt-get install -y cuda

# update PATH variables
{
    echo -e "\nexport PATH=/usr/local/cuda/bin:\$PATH";
    echo -e "export LD_LIBRARY_PATH=/usr/local/cuda/lib64";
} >> ~/.bashrc

# reboot for CUDA
sudo reboot</code></pre>

After waiting about a minute for the reboot, `ssh` back into the Instance

You can download this code as [`cuda_check.sh`]({{ site.baseurl }}/media{{page.redirect_from}}/cuda_check.sh)
<a id="cuda-check">

<pre class="line-numbers language-bash"><code># install included samples and test cuda
ver=8.0 # version number -- will get a more robust method in a later edit
echo "CUDA version: ${ver}"
/usr/local/cuda/bin/cuda-install-samples-${ver}.sh ~/
cd NVIDIA\_CUDA-${ver}\_Samples/1\_Utilities/deviceQuery
make
./deviceQuery
</code></pre>

Make sure the test shows that a GPU exists - common errors are listed [here](#errors-gpu).
If you don't have a GPU then skip the next step or use a GPU EC2 Instance

<pre class="line-numbers language-bash"><code>#  set up the theano config file to use gpu by default
{
    echo -e "\n[global]\nfloatX=float32\ndevice=gpu";
    echo -e "[mode]=FAST_RUN";
    echo -e "\n[nvcc]";
    echo -e "fastmath=True";
    echo -e "\n[cuda]";
    echo -e "root=/usr/local/cuda";
}>> ~/.theanorc</code></pre>

Install any other dependencies you may require.

## Get `CuDNN`
To obtain `CuDNN` you must register with the NVIDIA developer programme [here][9].
The download page for `CuDNN` is [here][10] and it's simplest to download the latest 
**Library for Linux** to your local machine and `scp` it over to EC2 as follows

<pre class="line-numbers language-bash"><code>scp -r ~/Downloads/cudnn-8.0-linux-x64-v5.1.tar ubuntu@[DNS]:/home/ubuntu/</code></pre>

where the `[DNS]` needs to be entered and the filename will differ as the software is updated. 
Once the `scp` has transferred the file move to the active `ssh` terminal instance in EC2 and do
the following to install `CuDNN`

<pre class="line-numbers language-bash"><code>tar -xvf cudnn-8.0-linux-x64-v5.1-tgz
# use tar -xzf cudnn-8.0-linux-x64-v5.1-tgz if the extension is .tgz
cd cuda
sudo cp lib64/* /usr/local/cuda/lib64/
sudo cp include/* /usr/local/cuda/include/</code></pre>

Now add the following to enable [`CNMeM`][11]
<pre class="line-numbers language-python"><code>echo -e "\n[lib]\ncnmem=0.5" >> ~/.theanorc</code></pre>
A value between `0-1` allocates this fraction of GPU memory to `theano` so here we allocate 
50% to not be stingy.

Now check that `theano` is configured properly by opening `ipython` and running
<pre class="line-numbers language-python"><code>import theano.sandbox.cuda
theano.sandbox.cuda.use("gpu0")</code></pre>
which gave me the output
<pre class="language-terminal"><code>Using gpu device 0: Tesla K80 (CNMeM is enabled with initial size: 50.0% of memory, cuDNN 5105)</code></pre>

<a id="run">

# Run Code
Transfer the relevant code across the the Cloud e.g.

 - Pull from an existing `git` repository
 - `scp` files across
 
If you are running code in a Spot Instance, I would recommend saving results at runtime
and passing them back to your local machine. It is sensible to `pickle` the state of the neural net
at runtime so that you can easily continue the training process from a saved state rather than
having to run again from scratch.

<a id="close"></a>

# Close
Don't forget to Stop or Close the instance once it has completed the task! 

Make sure that you check the instance has been closed **in addition** to the Spot request 
in the dashboard! I received a 31 hour bill for an unclosed GPU Compute instance that I had 
thought I closed which was rather annoying. 

In theory this can be automated by running the following as root after code has been executed
<pre class="line-numbers language-bash"><code>shutdown -h now</code></pre>
but now I don't particularly trust the methodology in practice.

<a id="errors" />

# Common Errors

## CUDA Failures
A few common errors encountered with installing CUDA

<a id="errors-gpu" />

### No GPU

If no GPU exists you will receive the following output

<pre class="language-terminal"><code>./deviceQuery Starting...

CUDA Device Query (Runtime API) version (CUDART static linking)

NVIDIA: no NVIDIA devices found
cudaGetDeviceCount returned 30
-> unknown error
Result = FAIL
ubuntu@ip-172-31-36-215:~/NVIDIA_CUDA-8.0_Samples/1_Utilities/deviceQuery$ ./deviceQuery 
deviceQuery        deviceQuery.cpp    deviceQuery.o      Makefile           NsightEclipse.xml  readme.txt         
ubuntu@ip-172-31-36-215:~/NVIDIA_CUDA-8.0_Samples/1_Utilities/deviceQuery$ ./deviceQuery 
./deviceQuery Starting...

 CUDA Device Query (Runtime API) version (CUDART static linking)
 
NVIDIA: no NVIDIA devices found
cudaGetDeviceCount returned 30
-> unknown error
Result = FAIL</code></pre>

The resolution is to cancel the instance and get a GPU instance if you require CUDA support.

### Unknown symbol in module

This is a slightly more complicated issue that arose since CUDA 7.5

<pre class="language-terminal"><code>./deviceQuery Starting...

 CUDA Device Query (Runtime API) version (CUDART static linking)

modprobe: ERROR: could not insert 'nvidia_361_uvm': Unknown symbol in module, or unknown parameter (see dmesg)
cudaGetDeviceCount returned 30
-> unknown error
Result = FAIL</code></pre>

The resolution for this is fairly simple and means that you didn't install `linux-image-extra-virtual`
as above. This is probably because you followed one of the guides in the references which are
now [out of date][7]. 

Simply run this line

<pre class="line-numbers language-bash"><code># install the required library
sudo apt-get install linux-image-extra-virtual

# restart instance
sudo reboot</code></pre>

then wait a minute or so for a restart and `ssh` back in and run the [CUDA check](#cuda-check)
again which should give the following at the end of the output

<pre class="language-terminal"><code>deviceQuery, CUDA Driver = CUDART, CUDA Driver Version = 8.0, CUDA Runtime Version = 8.0, NumDevs = 1, Device0 = Tesla K80
Result = PASS</code></pre>

<a id="refs">

# References

 - [Amazon Web Services][1]
 - [`theano` Docs][2]
 - [Ubuntu][3]
 - [Installing CUDA, OpenCL, and PyOpenCL on AWS EC2][4]
 - [How to install Theano on Amazon EC2 GPU instances for deep learning][5]
 - [StackOverflow: Self-Terminating AWS EC2 Instance][6]
 - [StackOverflow: ERROR: could not insert 'nvidia_361_uvm': Unknown symbol in module][7]
 - [NVIDIA Forums: Error installing nvidia drivers on x86_64 amazon ec2 gpu cluster (T20 GPU)][8]
 - [NVIDIA Developer Programme][9]
 - [CuDNN Download page][10]
 - [Theano Docs: CNMeM][11]

[1]: https://aws.amazon.com
[2]: http://theano.readthedocs.io
[3]: https://www.ubuntu.com
[4]: http://vasir.net/blog/opencl/installing-cuda-opencl-pyopencl-on-aws-ec2
[5]: http://markus.com/install-theano-on-aws/
[6]: http://stackoverflow.com/a/10542456/4013571
[7]: http://stackoverflow.com/a/34241135/4013571
[8]: https://devtalk.nvidia.com/default/topic/547588/error-installing-nvidia-drivers-on-x86_64-amazon-ec2-gpu-cluster-t20-gpu-/
[9]: https://developer.nvidia.com/accelerated-computing-developer
[10]: https://developer.nvidia.com/rdp/cudnn-download
[11]: http://deeplearning.net/software/theano/library/config.html#config.config.lib.cnmem