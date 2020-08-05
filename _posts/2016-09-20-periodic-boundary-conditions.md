---
layout:            post
title:             "Periodic Boundary Conditions for Lattices in Python"
menutitle:         "Periodic Boundary Conditions for Lattices in Python"
date:              2016-09-20 19:31:00 +0100
tags:              Periodic Boundary Conditions subclassing numpy.ndarray
category:          Python
author:            am
published:         true
redirect_from:     "/periodic-boundary-conditions/"
language:          EN
comments:          true
---

This is a useful method to force periodic boundary conditions in a `numpy` array. This is perhaps of interest for any sort of model where a continuum is required and can be approximated by a [torus](https://en.wikipedia.org/wiki/Torus).

The basic idea is to follow the official `numpy` guide for overloading the operators which is found [here](http://docs.scipy.org/doc/numpy/user/basics.subclassing.html).

# Assumptions / Simplifications
The key assumptions are that we will only require periodic boundary conditions where individual points in the array are selected. This is a sensible assumption and in fact if we don't do this it creates **CHAOS** when printing the overloaded arrays by causing infinite recursions.

# Wrap function
A simple function can be written with the `mod` function, `%` in basic python and generalised to operate on an `n`-dimensional tuple given a specific shape.

<pre class="line-numbers language-python"><code>def latticeWrapIdx(index, lattice_shape):
    """returns periodic lattice index 
    for a given iterable index
    
    Required Inputs:
        index :: iterable :: one integer for each axis
        lattice_shape :: the shape of the lattice to index to
    """
    if not hasattr(index, '__iter__'): return index         # handle integer slices
    if len(index) != len(lattice_shape): return index  # must reference a scalar
    if any(type(i) == slice for i in index): return index   # slices not supported
    if len(index) == len(lattice_shape):               # periodic indexing of scalars
        mod_index = tuple(( (i%s + s)%s for i,s in zip(index, lattice_shape)))
        return mod_index
    raise ValueError('Unexpected index: {}'.format(index))
</code></pre>

This is tested as:

<pre class="line-numbers language-python"><code>arr = np.array([[ 11.,  12.,  13.,  14.],
                [ 21.,  22.,  23.,  24.],
                [ 31.,  32.,  33.,  34.],
                [ 41.,  42.,  43.,  44.]])
test_vals = [[(1,1), 22.], [(3,3), 44.], [( 4, 4), 11.], # [index, expected value]
             [(3,4), 41.], [(4,3), 14.], [(10,10), 33.]]

passed = all([arr[latticeWrapIdx(idx, (4,4))] == act for idx, act in test_vals])
print "Iterating test values. Result: {}".format(passed)
</code></pre>

and gives the output of,
    
```text 
Iterating test values. Result: True
```

# Subclassing `numpy`
The wrapping function can be incorporated into a subclassed `np.ndarray` as described in the link in the introduction:


<pre class="line-numbers language-python"><code>class Periodic_Lattice(np.ndarray):
    """Creates an n-dimensional ring that joins on boundaries w/ numpy
    
    Required Inputs
        array :: np.array :: n-dim numpy array to use wrap with
    
    Only currently supports single point selections wrapped around the boundary
    """
    def __new__(cls, input_array, lattice_spacing=None):
        """__new__ is called by numpy when and explicit constructor is used:
        obj = MySubClass(params) otherwise we must rely on __array_finalize
         """
        # Input array is an already formed ndarray instance
        # We first cast to be our class type
        obj = np.asarray(input_array).view(cls)
        
        # add the new attribute to the created instance
        obj.lattice_shape = input_array.shape
        obj.lattice_dim = len(input_array.shape)
        obj.lattice_spacing = lattice_spacing
        
        # Finally, we must return the newly created object:
        return obj
    
    def __getitem__(self, index):
        index = self.latticeWrapIdx(index)
        return super(Periodic_Lattice, self).__getitem__(index)
    
    def __setitem__(self, index, item):
        index = self.latticeWrapIdx(index)
        return super(Periodic_Lattice, self).__setitem__(index, item)
    
    def __array_finalize__(self, obj):
        """ ndarray.__new__ passes __array_finalize__ the new object, 
        of our own class (self) as well as the object from which the view has been taken (obj). 
        See
        http://docs.scipy.org/doc/numpy/user/basics.subclassing.html#simple-example-adding-an-extra-attribute-to-ndarray
        for more info
        """
        # ``self`` is a new object resulting from
        # ndarray.__new__(Periodic_Lattice, ...), therefore it only has
        # attributes that the ndarray.__new__ constructor gave it -
        # i.e. those of a standard ndarray.
        #
        # We could have got to the ndarray.__new__ call in 3 ways:
        # From an explicit constructor - e.g. Periodic_Lattice():
        #   1. obj is None
        #       (we're in the middle of the Periodic_Lattice.__new__
        #       constructor, and self.info will be set when we return to
        #       Periodic_Lattice.__new__)
        if obj is None: return
        #   2. From view casting - e.g arr.view(Periodic_Lattice):
        #       obj is arr
        #       (type(obj) can be Periodic_Lattice)
        #   3. From new-from-template - e.g lattice[:3]
        #       type(obj) is Periodic_Lattice
        # 
        # Note that it is here, rather than in the __new__ method,
        # that we set the default value for 'spacing', because this
        # method sees all creation of default objects - with the
        # Periodic_Lattice.__new__ constructor, but also with
        # arr.view(Periodic_Lattice).
        #
        # These are in effect the default values from these operations
        self.lattice_shape = getattr(obj, 'lattice_shape', obj.shape)
        self.lattice_dim = getattr(obj, 'lattice_dim', len(obj.shape))
        self.lattice_spacing = getattr(obj, 'lattice_spacing', None)
        pass
    
    def latticeWrapIdx(self, index):
        """returns periodic lattice index 
        for a given iterable index
        
        Required Inputs:
            index :: iterable :: one integer for each axis
        
        This is NOT compatible with slicing
        """
        if not hasattr(index, '__iter__'): return index         # handle integer slices
        if len(index) != len(self.lattice_shape): return index  # must reference a scalar
        if any(type(i) == slice for i in index): return index   # slices not supported
        if len(index) == len(self.lattice_shape):               # periodic indexing of scalars
            mod_index = tuple(( (i%s + s)%s for i,s in zip(index, self.lattice_shape)))
            return mod_index
        raise ValueError('Unexpected index: {}'.format(index))
</code></pre>


# Testing

Testing demonstrates the lattice overloads correctly,

<pre class="line-numbers language-python"><code>arr = np.array([[ 11.,  12.,  13.,  14.],
                [ 21.,  22.,  23.,  24.],
                [ 31.,  32.,  33.,  34.],
                [ 41.,  42.,  43.,  44.]])
test_vals = [[(1,1), 22.], [(3,3), 44.], [( 4, 4), 11.], # [index, expected value]
             [(3,4), 41.], [(4,3), 14.], [(10,10), 33.]]

periodic_arr  = Periodic_Lattice(arr)
passed = (periodic_arr == arr).all()
passed *= all([periodic_arr[idx] == act for idx, act in test_vals])
print "Iterating test values. Result: {}".format(passed)
</code></pre>

and gives the output of,
    
```text 
Iterating test values. Result: True
```

Finally, using the code provided in the initial problem we obtain:

```text 
True
error
error
```

# Performance Gains
For highly optimised code, where the bulk computation is offloaded to the `C++` side of `numpy` or some low-level library, you may notice that a large amount of computation time is spent in `__array_finalize__`.

In this high performance context, every line of `python` code will have an impact on the runtime and as so a good way of skipping several lines is with the following hack:

<pre class="line-numbers language-python"><code>def __array_finalize__(self, obj):
    """ ndarray.__new__ passes __array_finalize__ the new object, 
    of our own class (self) as well as the object from which the view has been taken (obj). 
    """
    if obj is None: return

    try: # this is a way faster method of doing this
        self.lattice_shape   = obj.lattice_shape        # getattr(obj, 'lattice_shape', obj.shape)
        self.lattice_dim     = obj.lattice_dim          # getattr(obj, 'lattice_dim', len(obj.shape)) 
        self.lattice_spacing = obj.lattice_spacing      # getattr(obj, 'lattice_spacing', None)
    except: 
        self.lattice_shape   = obj.shape
        self.lattice_dim     = len(self.lattice_shape)
        self.lattice_spacing = None
    pass
</code></pre>

This won't be needed in 99% of usage cases though and and argument could be made that if this is having such an impact then the whole array should be in `C++` itself.

If you have any ideas on improving this last section then see my [StackOverflow post](http://stackoverflow.com/q/38875125/4013571) which is currently unanswered at the time of writing!