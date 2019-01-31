import numpy as np 

#Exam1
a = np.arange(10)
s = slice(2, 7, 2)      # Define a slice object with start, stop and step values 2, 7, 2
print(type(s))
print(a[s])

#Exam2

b = a[2:7:2]
print(b)

#Exam3
c = a[5]                # Slice single item
print(c)

#Exam4
d = a[2:]               # Slice items startng from index
print(d)

#Exam5
e = a[2:5]              # Slice items between indexes
print(e)

#Exam6
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr[1:])            # Slice items starting from index

