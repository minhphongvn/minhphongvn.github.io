---
layout:            post
title:             "High Frequency Data Storage"
menutitle:         "High Frequency Data Storage"
date:              2016-11-07 18:40:00 +0000
tags:              HDF5 MySQL High Frequency Data
category:          Python
author:            am
published:         false
redirect_from:     "/2016-11-07-high-freq-data-storage/"
language:          EN
comments:          true
---

Storing data efficiently is the bane of my life: It is boring and mundane but doing it inefficiently
 can have dire consequences.

# Contents
{:.no_toc}

* This will become a table of contents (this text will be scraped).
{:toc}
 
# Specifications
The following specifications are required for a decent solution

 - **Realtime data** Needs fast read / write*
 - **Limited Storage** Must be space efficient
 - **Simplicity** I want a fast, simple solution

# Options
I have ordered the performance of each data format with respect to required tasks

| :--- | :---: | :---: | :---: | :---: | :---: |
| **Task** | **`.txt`** | **`SQL`** | **`cPickle`** | **`HDF5`** | **`ASDF`** |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Bulk Read / Write | 4 | 5 | 3 | 1 | 2 |
| Last Item Read / Write | 1 | 2 | 5 | 3 | 4 |
| Implementation | 1 | 5 | 2 | 3 | 4 |
| Disk Size | 5 | 4 | 3 | 1 | 1 |

## `SQL`

The main advantage of `SQL` is the ability to push data to a remote location so that future 
queries upon the data do not require requests to the host machine.
  
## `HDF5` / `ASDF`
These both offer extremely fast read / write speeds. `HDF5` has the added benefit of a 
[`RESTful` interface][6] whereas  `ASDF` can contain more metadata but is slower as a result.

## `.txt` and binary formats
The binary formats seem the worst in terms of both performance and disk use. However, they
offer the massive advantage of being able to store python `class` objects through `dill`.
The `.txt` file format is the fastest for writing or reading single lines but has the worst disk 
usage and bad bulk read / writing speed.

# Choice for 1D Runtime Data
The update frequency is a key parameter. Assume an update frequency far greater than tic
 intervals. Thus there needs to be some process of efficiently capturing the data and transmitting
 at the update frequency in packets. 

## Monitoring in Realtime
 Here `SQL` actually looks like a good option in combination with a queuing process.
 
 With most virtual machines, requests are chargeable after a specific limit. This makes
  sending thousands of `SQL` commands highly undesirable so a sensible update frequency 
  should be chosen.

## Monitoring after a Run
Here `HDF5` looks like the better option again. This is because the update frequency is 
effectively equal to the length of the run so only one large request needs to be made.

# Choice for Large n-dim Arrays
Firstly, `MySQL` doesn't provide support `ARRAY` formats but it can be simulated by parsing a
string representing an array to a `VARCHAR` entry.

It seems that the format choice for large n-dim arrays should be `HDF5`.
I don't see clear benefits of `ADSF`. The main issue being the far slower write times.

If this is required in realtime for monitoring, it seems that the `HDF5` data could be parsed
to a `VARCHAR` entry in a table with an indexing column.

# References
 - [HDF5 Docs: Quick Start Guide][1]
 - [Moving away from HDF5][2]
 - [Should you use HDF5][3]
 - [ASDF: A new data format for astronomy][4]
 - [`HDF5` vs. `SQL` vs. `CSV`][5]
 - [HDF5 Server: H5Serv][6]
 - [HDF5 Docs: Quick Start Guide][7]
 - [`pyasdf` docs][8]
 - [StackOverflow: brew install mysql on mac os][9]
 
[1]: http://docs.h5py.org/en/latest/quick.html
[2]: http://cyrille.rossant.net/moving-away-hdf5/
[3]: http://cyrille.rossant.net/should-you-use-hdf5/
[4]: http://dx.doi.org/10.1016/j.ascom.2015.06.004
[5]: https://statcompute.wordpress.com/tag/hdf5/
[6]: https://github.com/HDFGroup/h5serv
[7]: http://docs.h5py.org/en/latest/quick.html
[8]: http://pyasdf.readthedocs.io/en/latest/index.html
[9]: http://stackoverflow.com/a/6378429/4013571