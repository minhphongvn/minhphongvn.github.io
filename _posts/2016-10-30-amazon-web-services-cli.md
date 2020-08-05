---
layout:            post
title:             "Launch EC2 GPU Cloud Instances from CLI"
menutitle:         "Launch EC2 GPU Cloud Instances from CLI"
date:              2016-10-30 05:31:00 +0000
tags:              EC2 CLI GPU Cloud
category:          Deep Learning
author:            am
published:         true
redirect_from:     "/2016-10-30-amazon-web-services-cli/"
language:          EN
comments:          true
---

This guide builds up to launching an arbitrary number of GPU cloud instances with
pre-loaded parameters. This allows for the distribution of lengthy tasks onto CUDA cores. This is
extremely useful for running a series of Deep Neural Networks with different parameterisations !

You will need an AWS account set up: See [previous blog][2]

# Contents
{:.no_toc}

* This will become a table of contents (this text will be scraped).
{:toc}

# Set Up IAM Access Key
To use the CLI you need an IAM access key and code pair

 - Navigate the [AWS IAM portal] [3]
 - Select **Users** in the left navigation pane
 - **Create New User**
 - Enter a user name & click **Create**
 - **Download Credentials** and store *securely*

# Install with `pip`
This is the simplest method if you have `pip`


<pre class="line-numbers language-terminal"><code>pip install awscli</code></pre>

add the flag `--user` if you don't have `root` access. See the [docs][3] for other installation 
options. To check the installation

    aws --version
    aws-cli/1.11.10 Python/2.7.12 Darwin/16.1.0 botocore/1.4.67

# Configure CLI
Configure the default user by the command `aws configure` as follows

    aws configure
    AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
    AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
    Default region name [None]: us-west-2
    Default output format [None]: json

A list of region codes can be found [here][5]

this creates two files at `~/.aws`. This `bash` command will show the simple contents

<pre class="line-numbers language-bash"><code>for f in $(ls ~/.aws/)
    do echo -e "# start ~/.aws/$f"
    cat ~/.aws/$f;echo -e "# end file\n"
done</code></pre>

which could be edited by either running `aws configure` or editing the contents directly

    # start ~/.aws/config
    [default]
    region = us-west-2
    # end file
    
    # start ~/.aws/credentials
    [default]
    aws_access_key_id = AKIAIOSFODNN7EXAMPLE
    aws_secret_access_key = wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
    # end file

See the [docs][6] for specifying additional users with different regions and keys.

Enable command completion by adding the following lines to `~/.bash_profile`

<pre class="line-numbers language-bash"><code># This is for the amazon web services CLI to enable autocompletion
complete -C '/usr/local/bin/aws_completer' aws
export PATH=/usr/local/bin/aws:$PATH</code></pre>

now refresh the `~/.bash_profile` by

<pre class="language-bash"><code>source ~/.bash_profile</code></pre>

see the [docs][7] if you installed without `pip`. Check the path to `aws` is correct by 
`which aws`.

You can test by entering `aws s` and hitting `TAB`. I found the autocompletion was bit rubbish. 
I had to `TAB` twice for it to display the first time

# Create Security Group, Key-Pair and Role

The following command creates the security group `example-name` with
 `an example description`

<pre class="language-bash"><code>aws ec2 create-security-group \
    --group-name example-name \
    --description "an example description"</code></pre>

then you can add a rule to allow `ssh` traffic over port `22` for a specific ip range specified by
a CIDR (see below)

<pre class="language-bash"><code>aws ec2 authorize-security-group-ingress\
     --group-name example-name \
     --protocol tcp \
     --port 22 \
     --cidr 0.0.0.0/0</code></pre>

If you're lazy, leave it as is.To be more secure, determine your CIDR code from a range of IP
addresses from your router using the `python` module [`netaddr`][8]

<pre class="line-numbers language-python"><code>import netaddr
start_ip = "63.223.64.0" # an example start ip
end_ip = "63.223.127.255"  # an example end ip
cidrs = netaddr.iprange_to_cidrs(start_ip, end_ip)
for cidr in cidrs: print cidr</code></pre>

You can now test this worked by running

<pre class="language-bash"><code>aws ec2 describe-security-groups</code></pre>

which will probably fail with the following result

    An error occurred (UnauthorizedOperation) when calling the DescribeSecurityGroups operation: You are not authorized to perform this operation.

You can [fix this][9] by navigating again to the [Amazon IAM portal][3]

 - Select **Policies** (and **Get Started** if you haven't visited this page before)
 - Filter `Policy Type` by `admin` in the top search bar
 - Select `AdministratorAccess`
 - Click **Policy Actions** and **Attach**

<figure>
  <img src="{{ site.baseurl }}/media{{page.redirect_from}}set-policy.png" />
  <figcaption>This vital step is not covered in the AWS CLI guide</figcaption>
</figure>

 - Select your username if it asks you to
 - **Attach Policy**
 - Wait 10 secs or so and retry the command above which should return `JSON`

If any errors are encountered, visit the [StackOverflow thread][9] as the required fix may change 
over time.

# Create an Instance from the CLI

It is possible to create an `ssh` key directly through the CLI

<pre class="line-numbers language-bash"><code>aws ec2 create-key-pair \
    --key-name example-key-name \
    --query 'KeyMaterial' \
    --output text \
> ~/Downloads/example-key-name.pem
chmod 400 ~/Downloads/example-key-name.pem</code></pre>

This means you will have a new key for each session which is a bit more secure than the global
 `ssh` key method described in the [previous guide][2].
 
 A new instance can be created with the following command, which returns the `InstanceId` when
 successful. Note that this is a **Free Tier** request so it won't bill and is ideal for playing with the 
 CLI

<pre class="language-bash"><code>aws ec2 run-instances \
    --image-id ami-ed82e39e \
    --security-group-ids example-name \
    --count 1 \
    --instance-type t2.micro \
    --key-name example-key-name \
    --query 'Instances[0].InstanceId'</code></pre>

The full `JSON` response is filtered by `--query 'Instances[0].InstanceId'` where
`'Instances[0].InstanceId'` means selecting the first `JSON` value for the key `Instances`
and returning the value for the key `InstanceId`. More details on `--query` can be found in
the [docs][10]. When specifying an `--image-id` make sure it corresponds to the correct region.
In the case of an error code of `(InvalidAMIID.NotFound)` try specifying 
`--region eu-west-1` or the relevant region code.

The public IP for the instance can be returned by subsequently running

<pre class="language-bash"><code>aws ec2 describe-instances \
        --instance-ids yourInstanceId \
        --query 'Reservations[0].Instances[0].PublicIpAddress'</code></pre>

alternatively, the DNS can be found by using 

<pre class="language-bash"><code>--query 'Reservations[0].Instances[0].PublicDnsName'</code></pre>

This can simply be adjusted to return multiple instances with the following syntax

<pre class="language-bash"><code>aws ec2 describe-instances --query 'Reservations[0].Instances[*].PublicDnsName'</code></pre>

# Connect
Connecting is straightforward and simply requires

<pre class="language-bash"><code>ssh -i ~/Downloads/example-key-name.pem ubuntu@[PublicIp_or_DNS]</code></pre>

and you can connect either the IP or the DNS specified. If you used a default key stored in 
`~/.ssh` then `-i /path/to/key.pem` isn't required. If you can't connect and get 
`Operation timed out` then try the following

<pre class="language-bash"><code>aws ec2 describe-instances \
    --instance-id yourInstanceId \
    --query 'Reservations[0].Instances[0].NetworkInterfaces[0].Groups[0].GroupName'</code></pre>

and if it returns `"default"` then you messed up and blocked all incoming traffic which nicely
ties into the last section

# Terminating an Instance
An instance may be terminated by

<pre class="language-bash"><code>aws ec2 terminate-instances --instance-ids instance_id</code></pre>

where multiple instances may be terminated through

<pre class="language-bash"><code>aws ec2 terminate-instances \
    --instance-ids instance_id0 instance_id1 instance_id2</code></pre>

which is equivalent to specifying the full JSON

<pre class="language-bash"><code>--instance-ids ["instance_id0", "instance_id1", "instance_id2"]</code></pre>

for more shorthand notation see the [docs][11]

# Tagging Instances
Instances may only be tagged after they are created through the command

<pre class="language-bash"><code>aws ec2 create-tags --resources=yourInstanceId --tags Key=TestName,Value=TestName</code></pre>

however, it is possible to do this in one line through `xargs` and shell script as

<pre class="line-numbers language-bash"><code>aws ec2 run-instances \
    --image-id ami-ed82e39e \
    --security-group-ids example-name \
    --count 1 \
    --instance-type t2.micro \
    --key-name example-key-name \
    --query 'Instances[0].InstanceId' | \
xargs -I {} sh -c "
    echo 'InstanceId:'{}
    aws ec2 create-tags \
        --resources={} \
        --tags Key=Name,Value=TestName"</code></pre>

annoyingly there is no confirmation that the request was successful so I prefer to use this `sh`
code (you [cannot](http://stackoverflow.com/q/40335292/4013571) do this with `xargs`)

<pre class="line-numbers language-bash"><code>SEC_GRP=example-name
KEY=example-key-name
ID=$(aws ec2 run-instances \
    --image-id ami-ed82e39e \
    --security-group-ids $SEC_GRP \
    --count 1 \
    --instance-type t2.micro \
    --key-name $KEY \
    --query 'Instances[0].InstanceId' \
    --output text)
echo 'Started InstanceId: '$ID
echo 'Creating Tags ...'
aws ec2 create-tags \
    --resources=$ID \
    --tags Key=Name,Value=TestName
echo 'Tags created: Key, Value'
aws ec2 describe-instances \
    --instance-id $ID \
    --query 'Reservations[0].Instances[0].Tags' \
    --output text</code></pre>

# Spot Requests with CLI
Spot requests can be requested with the following command

<pre class="language-bash"><code>aws ec2 request-spot-instances \
    --spot-price "0.050" \
    --instance-count 2 \
    --block-duration-minutes 120 \
    --type "one-time" \
    --launch-specification file://~/Desktop/test.json \
    --query 'SpotInstanceRequests[*].SpotInstanceRequestId' \
    --output text</code></pre>

This will output the `SpotInstanceRequestIds` that manages requests

- `--spot-price` is specifying a max bid price of `USD$ 0.05`
- `--instance-count 2` looks to launch `2` instances with the same parameters
- `--block-duration-minutes 120` means the request will stop at `120` if not already 
    terminated or interrupted by a spot price rise
- `--type "one-time"` means that when interrupted / terminated no further instances will be 
    launched

for more details and customisations see the [docs][12]. I would also recommend checking the
 docs to make sure `--spot-price` isn't changed to specify as units of `1000*USD$` !

The file `~/Desktop/test.json` should contain something similar to

<pre class="line-numbers language-json"><code>{
  "ImageId": "ami-0d77397e",
  "KeyName": "example-key-name",
  "SecurityGroupIds": [ "sg-youSecurityGroupID" ],
  "InstanceType": "m4.large",
  "Placement": {
      "AvailabilityvZone": "eu-west-1a"
    }
}</code></pre>

which specifies that we want `m4.large` instances in the `eu-west-1a` (Ireland) region with
the AMI `ami-0d77397e` (64bit Ubuntu) more detailed examples of `--launch-specification` 
files can be found [here][13]

You can view the IDs of these requests by

<pre class="language-bash"><code>aws ec2 describe-spot-instance-requests \
    --query SpotInstanceRequests[*].{ID:InstanceId}</code></pre>

If one or more are `NULL` then view the status by

<pre class="language-bash"><code>aws ec2 describe-spot-instance-requests \
    --query SpotInstanceRequests[*].Status.Message</code></pre>

which will most likely show something like

    [
        "Your Spot request price of 0.05 is lower than the minimum required Spot request fulfillment price of 0.081.", 
        "Your Spot request price of 0.05 is lower than the minimum required Spot request fulfillment price of 0.081."
    ]

# Getting the Spot Prices 
The current spot price can be obtained from an API at this endpoint which
can be handled in `python`

<pre class="line-numbers language-python"><code>import json
import operator
import requests

machine_type = 'p2.xlarge'
api_url = "http://spot-price.s3.amazonaws.com/spot.js"

print "Loading spots for Machine Type: {} ...".format(machine_type)
res = requests.get(api_url)
cleaned = res.content[len('callback('):-len(');')]
result = json.loads(cleaned)

# get all spots by region
reg_machine_spots = {
    region['region']:{
        size['size']: [
            os['prices']['USD'] 
            for os in size['valueColumns'] if os['name']=='linux'
        ][0] 
        for it in region['instanceTypes'] for size in it['sizes']
    }
    for region in result['config']['regions']
}

# get all regional spots
spots = {
    region: prices[machine_type] 
    for region,prices in reg_machine_spots.iteritems()
}

# print the prices sorted lowest first
ami_spots = sorted(spots.items(), key=operator.itemgetter(1))
for reg,spot in ami_spots: print reg.ljust(15) + spot</code></pre>

My command line version is available [here]({{ site.baseurl }}/media{{page.redirect_from}}/cheapest_spot.py)
and can be run as

    ./cheapest_spot.py -t p2.xlarge

check the [StackOverflow post][14] if the link is outdated but this should return something like the 
following and is very helpful for determining instant prices

    Loading spots for Machine Type: p2.xlarge ...
    us-west-2      0.1315
    eu-ireland     0.1643
    us-east        0.1887
    apac-sin       N/A*
    us-west        N/A*
    ap-northeast-2 N/A*
    us-east-2      N/A*
    apac-tokyo     N/A*
    apac-syd       N/A*
    ap-south-1     N/A*
    eu-central-1   N/A*
    sa-east-1      N/A*

It is also possible to obtain the historic spot prices using the CLI as follows

<pre class="language-bash"><code>aws ec2 describe-spot-price-history \
    --instance-types m1.xlarge \
    --product-description "Linux/UNIX (Amazon VPC)" \
    --start-time 2016-10-31T03:00:00 \
    --end-time 2016-10-31T03:16:00 \
    --query 'SpotPriceHistory[*].[Timestamp,SpotPrice]'</code></pre>

The historic time is limited and check the [docs][15] for latest details

# Terminate Spot Instances

To cancel spot instance requests

<pre class="language-bash"><code>aws ec2 cancel-spot-instance-requests \
    --spot-instance-request-ids sir-08b93456 sir-08b93458</code></pre>

where `sir-08b93456 sir-08b93458` are *not* the `instanceIds`

The instances themselves should also then be terminated

<pre class="language-bash"><code>aws ec2 terminate-instances \
    --instance-ids i-1234567890abcdef0 i-0598c7d356eba48d7</code></pre>

here the instance IDs are made explicit to differentiate them from the Spot Instance ID. Make
sure to do both as you may end up having instances running without being aware !

# References
 - [AWS Guide][1]
 - [Set Up Amazon Elastic Compute Cloud (EC2)][2]
 - [AWS IAM Portal][3]
 - [AWS Guide: Installing AWS CLI][4]
 - [AWS Region List][5]
 - [AWS Guide: CLI Multiple Profiles][6]
 - [AWS Guide: CLI Completion][7]
 - [`netaddr` docs][8]
 - [StackOverflow: AWS CLI Client.UnauthorizedOperation even when keys are set][9]
 - [AWS Guide: Filtering with the `--query` option][10]
 - [AWS Guide: Shorthand Syntax][11]
 - [AWS Guide: Using Spot Instance Request][12]
 - [AWS Guide: Spot Request Examples][13]
 - [StackOverflow: get ec2 pricing programmatically?][14]

 [1]: http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html
 [2]: {% post_url 2016-10-25-set-up-amazon-ec2 %}
 [3]: https://console.aws.amazon.com/iam/home?#home
 [4]: http://docs.aws.amazon.com/cli/latest/userguide/installing.html#install-with-pip
 [5]: http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region
 [6]: http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html#cli-multiple-profiles
 [7]: http://docs.aws.amazon.com/cli/latest/userguide/cli-command-completion.html
 [8]: https://pythonhosted.org/netaddr/api.html#netaddr.iprange_to_cidrs
 [9]: http://stackoverflow.com/a/31323864/4013571
 [10]: http://docs.aws.amazon.com/cli/latest/userguide/controlling-output.html#controlling-output-filter
 [11]: http://docs.aws.amazon.com/cli/latest/userguide/shorthand-syntax.html
 [12]: http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-requests.html
 [13]: http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-request-examples.html
 [14]: http://stackoverflow.com/questions/7334035/get-ec2-pricing-programmatically