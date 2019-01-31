import numpy as np 

# basic declare
x = np.array([1, 2, 3])

# declare with argument
a = np.array([1, 2], dtype = np.float64)   # define array with float64
print(type(a))                             # print type of a
print(type(a[0]))                          # print type of a[0]; print <class 'numpy.float64'>


# init special one-dimension array
one = np.ones((3,))
print(one)

zero = np.zeros(3)
print(zero)

oneT = np.ones((3,1))
print(oneT)

dot_2D = np.ones((1,1))
print(dot_2D)

# Cap so cong
arange = np.arange(3)
print(arange)

my_arange = np.arange(3,9)                 # Tao mang cac so lien tiep tu m den n -1, dung np.arange(m,n)
print(my_arange)

my_array = np.arange(0, 1, 0.1)            # Tao mot cap so cong voi phan tu dau la a, cong sai d, phan tu cuoi la so duong lon nhat nho hon b ta dung ham np.arange(a,b,d)
print(my_array)

# Ex1

exp_array = np.arange(0,11)
first = 2
result = first ** exp_array
print(result)

#1.4    Truy cap kich thuoc mang mot chieu

''' Kich thuoc cua mot mang numpy x noi chung duoc xac dinh bang numpy.array.shape
'''
print(x.shape)

#1.4.2  Chi so

''' Moi thanh phan tring mang 1 chieu tuong ung voi mot chi so, bat dau bang 0
'''

print(x[0])                                # Doc tung phan tu cua vector

#1.4.4  Chi so nguoc

''' Trong python co mot diem dac biet la Chi so nguoc. Cho mot mang 1 chieu co d phan tu
De truy cap vao phan tu cuoi cung cua mang nay, t co the dung chi so -1
'''
d = np.random.random((3,))                 # Create a random vector

print(d[-1])

#1.5    Truy caapj nhieu phan tu cua mang mot chieu

#1.5.1  Doc

array = np.arange(10) * 0.5
idx = [1, 3, 5, 7]                         # Create array index 
print(array[idx])

''' Ngoai ra cach danh chi so cua mang numpy cung su dung cac quy tac khac giong nhu
cacsh danh chi so cua mot list
'''

print(array[:3])                           # print first three elements
print(array[-3:])                          # print last three elements
print(array[1:4])                          # print elements with indexes 1, 2, 3

#1.5.2  Ghi

array[[1, 3, 5]] = 1                       # <=> array[1] = array[3] = array[5] = 1
array[-3:] = np.array([0, -1, -2])         # <=> array[-3] = 0, array[-2] = -1, array[-1] = -1
array[::2]                                 # return all elements with even indexes
print(array)
array[::-1]                                # reverse an array
print(array)

#1.9    Tich vo huong cua hai vectors - Norm 2

y = np.ones(3)
z = np.random.random(3)
print(np.dot(y,z))

#1.10   min, max, armin, argmax cua mang mot chieu
#1.10.1 min, max

print(np.min(z))
print(np.max(z))

#1.10.2 argmin, argmax
''' De tim chi so ma tai do mang mot chieu dat gias trij nhor nhat hay lon nhat ta co the su dung np.argmin, hoac np.argmax
'''
print(np.argmin(z))
print(np.argmax(z))