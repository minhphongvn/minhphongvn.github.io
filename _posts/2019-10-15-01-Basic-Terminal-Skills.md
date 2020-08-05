---
layout: post
title: "01: Basic Terminal Skills"
menutitle: "01: Basic Terminal Skills"
date: 2019-10-15 22:32 +0000
tags: Python Tutorial Learning
category: Python Tutorial
author: am
published: true
redirect_from: "/2019-10-15-01-Basic-Terminal-Skills/"
language: EN
comments: true
---

## Learning Outcomes
{:.no_toc}

 - Be able to find / open the terminal
 - Be able to navigate filesystem within the Terminal
 - Basic usage of linux commands

## Contents
{:.no_toc}

* This will become a table of contents (this text will be scraped).
{:toc}


# Opening the `Terminal`

Why do I care? Basically because all the self help on the internet will rely on you being able to reproduce what you messed up in a minimal example. A lot of errors at the early stages are often to do with set up and nothing to do with `python`. Being able to run code in a minimal way in the terminal will give you confidence in programming in `python` and be able to isolate `python` issues from mor generic setup or configuration issues which can be very difficult to otherwise debug.

## Opening a console on Mac OS X
OS X’s standard console is a program called `Terminal`. Open `Terminal` by navigating to Applications, then Utilities, then double-click the `Terminal` program. You can also easily search for it in the system search tool in the top right.

The command line `Terminal` is a tool for interacting with your computer. A window will open with a command line prompt message, something like this:

```sh
mycomputer:~ myusername$
```

## Opening a console on Windows
Window’s console is called the Command Prompt, named `cmd`. However it sucks. I would always recommend using `powershell`. An easy way to `powershell` to it is by using the key combination `Windows+R` (Windows meaning the windows logo button), which should open a Run dialog. Then type `powershell` and hit `Enter` or click Ok. You can also search for it from the start menu. It should look like:

```sh
C:\Users\myusername>
```

Window’s `powershell` is not quite as powerful as its counterparts on Linux and OS X but they've copied all the relevant parts that we will want to use


# Navigating around the `Terminal`

From this point onwards anything denoted like

```sh
$ program
```

will represent a `Terminal` interface (this is not python!). The above represents running a command named `program` in the `Terminal`.


## Moving around directories

These commands will soon become second nature & after some practice they are quite a lot faster than navigating the user interface file explorer!

Check what directory you are in

```sh
$ pwd
```

show what's in the current directory

```sh
$ ls
```

make a new directory

```sh
$ mkdir newdirectory
```

enter this directory

```sh
$ cd directory
```

go up one directory

```sh
$ cd ..
```

show whats inside the directory

```sh
$ ls directory/
```

remove a file

```sh
$ rm file.ext
```

Change the path (rename) a file (and / or extension)

```sh
$ mv directory/file.dat anotherdirectory/file2.csv
```

remove a directory (I probabaly wouldn't do this hastily!)

```sh
$ rm -r directory
```

The `-r` is a known as a flag. This modifies the behaviour of the program `rm`. IN this instance it allows `rm` 
to delete directories which is otherwise a risky default ability.

These are pretty much all the commands you need. Try to familiarise yourself with them.
All of these commands e.g. `ls`, `rm`, `mkdir` are all programs themselves that take in arguments from the command line depending on their operation.


# Exercises

Your *local* machine home directory is always denoted by `~/` (note the slashes are backwards in Windows so this is `~\`for Windows machines)

These exercises aim to get you more comfortable with using the command line rather than being an actual problem solving task

## Exercise 1.1: Creating directories
- `cd` into the directory `~`
- Create a new directory named `temp` in this directory

## Exercise 1.2: Renaming directories

Change the name of this directory to `pylrn`

You can test this worked by doing

```sh
$ ls ~/pyl*
```

the `*` will wildcard all text following it

## Exercise 1.3: Create a file with contents

Run the following command to create a new file

**Max OS X users do this**
```sh
$ touch ~/pylrn/test.py
$ echo print('Hello World') >> ~/pylrn/test.py
```

**Windows users do this**
```sh
$ "print('Hello World')" | Out-File ~/pylrn/test.py -encoding ascii
```

verify it is there with

```sh
$ ls ~/pylrn/*.py
```

# Next Topic
{:toc}

[02: Installing Python for Mac OS X / Windows](https://flipdazed.github.io/blog/python%20tutorial/02-Installing-Python-for-Mac-OS-X-Windows)
