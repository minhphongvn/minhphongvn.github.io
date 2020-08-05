---
layout: post
title: "How To Link C++ to Python with boost-python"
menutitle: "How To Link C++ to Python with boost-python"
date: 2016-10-27 17:40 +0100
tags: How To Boost-Python Python C++
category: Python
author: am
published: true
redirect_from: "/2016-10-27-boost-python-starter/"
language: EN
comments: true
---

This is a most basic starter with [`boost-python`][1] using [`homebrew`][2] with the following structure

* This will become a table of contents (this text will be scraped).
{:toc}

 All the source code can be found in [this repository][3].

# Assumptions

- Familiarity `python` as a minimum requirement
- Have [`homebrew`][2] installed
- `python 2.7`
- Vague `C/C++` knowledge i.e. be able to write a function!
- `Mac OS X `- I used El Capitan `10.11.6` at the time of writing

# Get `boost-python`
You can obtain the correct [`boost-python`][1] through [`homebrew`][2] via the command:

<pre class="language-bash"><code>brew install boost --with-python --build-from-source</code></pre>
	
I think `brew install boost` should work but it's a big install and life is short to do it twice

<a id="hello">

# A simple example: `"Hello World!"`

The following code wraps the `C++` function `greet()` as a python extension 
named `hello_ext`. Save this as a `.cpp` file. To avoid ambiguity with internal functions 
name it something random e.g. `hippopotaplusplus.cpp`

<pre class="line-numbers language-cpp"><code>#include &lt;boost/python.hpp&gt;

char const* greet()
{
   return "Greetings!";
}

BOOST_PYTHON_MODULE(hello_ext)
{
    using namespace boost::python;
	def("greet", greet);
}</code></pre>

 - This code **cannot be called until it is compiled** - see below
 - `greet()` is exclusively a `C++` function
 - `BOOST_PYTHON_MODULE(hello_ext)` defines a module that can be called from `python` as 
     
    <pre class="language-python"><code>import hello_ext</code></pre>
    
 - `using namespace boost::python` allows`def` instead of `boost::python::def` each time
 - The method [`boost::python::def`][4] defines the second argument (the `C++` function) `greet` 
    as a `python` function (named by the string) `"greet"`. We call this function in `python` as
    
    <pre class="language-python"><code>import hello_ext
hello_ext.greet()</code></pre>
    
    if we had used `def("example", greet);`  we would call in `python` as 
    `hello_ext.example()`

## Compiling with `Python`

The following `python` module can be used to compile and link the code in 
`hippopotaplusplus.cpp` to a `python`-friendly module

<pre class="line-numbers language-python"><code>from distutils.core import setup
from distutils.extension import Extension

ext_instance = Extension(
    'hello_ext',
    sources=['hippopotaplusplus.cpp'],
    libraries=['boost_python-mt'],
)

setup(
    name='hello-world',
    version='0.1',
    ext_modules=[ext_instance])</code></pre>

 - The first `string` argument of `Extension` **must** match the `variable` declared in 
     the `.cpp` file by the line
     
    <pre class="language-cpp"><code>BOOST_PYTHON_MODULE(variable)</code></pre>
    
     in this case it is `hello_ext`. If this is incorrect, the code will compile but an attempt to `import`
     in `python` will produce the error 
     
    <pre class="language-ipython"><code>ImportError: dynamic module does not define init function</code></pre>
    
 - The augment `sources` defines the `cpp` file that is to be  compiled
 - The argument of `libraries=['boost_python-mt']` is the required library installed by `homebrew`
 - The argument to `ext_modules=[ext_instance])` points to the instance of `Extension`
 - The `name` and `version` are really for building packages and not necessary here
 - For more details, the [official docs][[5]] for `distutils` are well written

## Running
The code is compiled with `python` through the following command

<pre class="language-bash"><code>python setup.py build_ext --inplace</code></pre>

which will create the following `build/` directory and file
    	
    build/
    hello_ext.so

This can be directly now called by python with

<pre class="line-numbers language-python"><code>import hello_ext
hello_ext.greet()</code></pre>

# Wrapping multiple functions in a module

We can define several functions in external files by moving `greet` to its own file `greet.cpp` and
creating another file with the function `meet` saved as `meet.cpp`

<pre class="line-numbers language-cpp"><code>char const* meet()
{
   return "Nice to meet you from Boost!";
}</code></pre>

We can link this in the following manner with `hippopotaplusplus.cpp` as

<pre class="line-numbers language-cpp"><code>#include &lt;greet.hpp&gt;
#include &lt;meet.hpp&gt;
#include &lt;boost/python.hpp&gt;

BOOST_PYTHON_MODULE(hello_ext)
{
    using namespace boost::python;
    def("greet", greet);
	def("meet", meet);
}</code></pre>

## Compiling
The `setup.py` file to compile the code is structured exactly the same as above

## Running
The running of the code is also exactly the same as above except now we can call both functions

<pre class="line-numbers language-python"><code>import hello_ext
hello_ext.greet()
hello_ext.meet()</code></pre>

# References

- [`boost-python`][1] docs
- [`homebrew`][2]
- [example source code][3]
- [`boost::python::def`][4] docs
- [`distutils`][5] docs

[1]: http://www.boost.org/doc/libs/1_37_0/libs/python/doc/index.html
[2]: http://brew.sh/
[3]: https://github.com/flipdazed/boost-python-hello-world/
[4]: http://www.boost.org/doc/libs/1_37_0/libs/python/doc/v2/def.html
[5]: https://docs.python.org/2.7/extending/building.html