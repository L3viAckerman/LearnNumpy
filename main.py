## Quick sort ##

# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quicksort(left) + middle + quicksort(right)

# print(quicksort([3,6,8,10,1,2,1]))


## Basic data type ##

# x = 3
# print(type(x))
# print(x)
# print(x + 1)
# print(x -2)
# print(x * 2)
# print(x ** 2)
# x += 1
# print(x)
# x *= 2
# print(x)
# y = 2.5
# print(type(y))
# print(y, y + 1, y * 2, y ** 2)


## Booleans ##

# t = True
# f = False
# print(type(t))
# print(t and f)
# print(t or f)
# print(not f)
# print(t != f)

## Strings ##

# hello = 'hello'
# world = 'world'
# print(hello)
# print(len(hello))
# hw = hello + ' ' + world
# print(hw)
# hw12 = '%s %s %d' % (hello, world, 12)
# print(hw12)

# s = "hello"
# print(s.capitalize())
# print(s.upper())
# print(s.rjust(7))
# print(s.center(7))
# print(s.replace('l', '(ell)'))

# print('   world '.strip())


## COntainers ##

# xs = [3, 2, 1]      # Create a list
# print(xs, xs[1])    # Prints "[3, 1, 2] 2"
# print(xs[-1])       # Negative indices count from the end of the list; prints "2"
# xs[2] = 'foo'       # List can contain elements of diffirent types
# print(xs)
# xs.append('bar')    # Add a new element to the end of the list
# print(xs)
# x = xs.pop()        # Remove and return the laste element of the list
# print(x, xs)


# ## Slicing ##

# nums = list(range(5))
# print(nums)
# print(nums[2:4])            # Get a slice from index 2 to 4 (exclusive1); prints "[2, 3]"
# print(nums[2:])             # Get a slice from index 2 to the end of list
# print(nums[:2])             # Get a slice from index 0 to 2 
# print(nums[:])              # Get a slice from whole list
# print(nums[:-1])            # Slice indices can be negative; prints "[0, 1, 2 , 3]"
# nums[2:4] = [8, 9]
# print(nums)

## Loops ##

# animals = ['cat', 'dog', 'monkey']
# for animal in animals:
#     print(animal)

# for idx, animal in enumerate(animals):
#     print('#%d: %s' %(idx + 1, animal))

## List comprehensions ##

# nums = [0, 1, 2, 3, 4]
# squares = [x ** 2 for x in nums]
# print(squares)

# even_squares = [x ** 2 for x in nums if x % 2 == 0]
# print(even_squares)

## Dictionaries ##

# A dictionary stores (key, value) pairs, similar to a Map in Java or an object i Javascript. You can use it like this:

# d = {'cat': 'cute', 'dog' : 'furry'}        # Create a new dictionaty with some data
# print(d['cat'])                             # Get an entry from a dictionary; print "cute"
# print('cat' in d)                           # Check if a dictionary has a given key; print "True"
# d['fish'] = 'wet'                           # Set an entry in a dictionary
# print(d['fish'])

# print(d.get('monkey', 'N/A'))               # Get an element with a default; print "N/A"
# print(d.get('fish', 'N/A'))                 # Get an element with a default; print "wet"
# del d['fish']                               # Remove an element from a dictionary
# print(d.get('fish', 'N/A'))                 # fish is no longer a key; print "N/A"

# ## Loops ##

# d = {'person' : 2, 'cat' : 4, 'spider' : 8}
# for animal in d:
#     legs = d[animal]
#     print('A %s has %d legs' %(animal, legs))

# ## Dictionary comprehensions

# nums = [0, 1, 2, 3, 4]
# even_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0}
# print(even_num_to_square)

# ## Set

# animals = {'cat', 'dog'}
# print('cat' in animals)         # Check if an element is in a set; prints 'True'
# print('fish' in animals)
# animals.add('fish')
# print('fish' in animals)
# animals.add('cat')
# print(len(animals))
# animals.remove('cat')
# print(len(animals))

# ## Loops

# for idx, animal in enumerate(animals):
#     print('#%d: %s' % (idx+1, animal))

# ## Set comprehensions

# from math import sqrt
# nums = {int(sqrt(x)) for x in range(30)}
# print(nums)

# ## In set, there is only extince element

## Tuples

## A tuple is an immutable ordered list of value. A tuple is in many ways similar to a list, one of the most importani diffences is that tuples can be used as keys in dictionaties
## and as elements of sets, while lists cannot. 

# d = {(x, x+1): x for x in range(10)}        # Create a dictionary with tuple keys
# t = (5, 6)
# print(type(t))
# print(d[t])
# print(d[(1, 2)])


## Funcions

# def sign(x):
#     if x > 0:
#         return 'positive'
#     elif x < 0:
#         return 'negative'
#     else: 
#         return 'zero'

# for x in [-1, 0, 1]:
#     print(sign(x))

# def hello(name, loud = False):
#     if loud:
#         print('HELLO, %s!' % name.upper())
#     else:
#         print('Hello, %s!' % name)


# hello('Bob')
# hello('Fred', loud=True)

## Classes

# class Greeter(object):

#     # Constructor
#     def __init__(self, name):
#         self.name = name        # Create an instance variable
    
#     # Instance method
#     def greet(self, loud = False):
#         if loud:
#             print('HELLO, %s!' % self.name.upper())
#         else:
#             print('Hello, %s!' % self.name)

# g = Greeter('Fred')

# g.greet()
# g.greet(loud = True)


## Numpy ##

# Numpy is the core library for scientific computing in Python. It provides a high-performance multidimensional arry object,
# and tools for working with these arrays. If you are already familiar with MATHLAB, you might find this tutorial useful to
# get started with Numpy

# Arrays

# A numpy array is a grid of values, all of the same type and is indexed by a tuple of nonnegative integers. The
# number of dimensions is the rank of the array, the shape of an array is a tuple of integers giving the size of the array along each dimension
# We can initialize numpy arrays from nested Python lists, and access elements using square brackets

# import numpy as np 

# a = np.array([1, 2, 3])
# print(type(a))
# print(a.shape)
# print(a[0], a[1], a[2])

# a[0] = 5
# print(a)


# b = np.array([[1, 2, 3], [4, 5, 6]])
# print(b.shape)
# print(b[0, 0], b[0, 1], b[1, 0])

# Create arrays using func

# import numpy as np 
# a = np.zeros((2,3))

# print(a)

# b = np.ones((1, 2))
# print(b)

# c = np.full((2,), 7)
# print(c)

# d = np.eye(2)
# print(d)

# e = np.random.random((3, 3))
# print(e)

# Array indexing

# Slicing: Similar to Python lists, numpy arrays can be sliced. Since arrays may be multidimensional, you must specify a slice for each  dimension of the array

import numpy as np 

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

b = a[:2, 1:3]
print(b)

print(a[0, 1])
b[0, 0] = 77

print(a[0, 1])
print(a[0][1])      # Same the upper

row_r1 = a[1, :]    # Rank 1 view of the second row of a
row_r2 = a[1:2, :]  # Rank 2 view of the second row of a

print(row_r1, row_r1.shape)
print(row_r2, row_r2.shape)

# We can make the same distinction when accessing columns of an array

col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print(col_r1, col_r1.shape)
print(col_r2, col_r2.shape)

