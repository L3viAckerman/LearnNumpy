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

## Loops ##
d = {'person' : 2, 'cat' : 4, 'spider' : 8}
for animal in d:
    legs = d[animal]
    print('A %s has %d legs' %(animal, legs))
