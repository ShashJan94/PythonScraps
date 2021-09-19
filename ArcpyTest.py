import numpy as np

'''print(np.version.version)
np.__config__.show()'''  # solution 1

'''np.info(np.add)'''  # solution2
'''def ZeroElementCheck():
 a1 = np.random.randint(0,10,size=(8))
 print(a1)
 if np.count_nonzero(a1)!=len(a1):
    return True
 return False
print(ZeroElementCheck())'''  # solution 3


'''def NonZeroElementCheck():
    a1 = np.random.randint(0, 2, size=(5))
    print(a1)
    if np.count_nonzero(a1):
        return True
    return False

print(NonZeroElementCheck())''' #solution 4
'''a = np.matrix(np.ones((10,10))*-1*np.inf)
b= np.matrix(np.zeros((10,10)))
print(a)
print(np.isfinite(a))
print(np.isinf(b))
print(np.isposinf(a))
print(np.isneginf(a))''' #Solution 5,6

''''a = np.matrix(np.random.randint(5,15,size=(3,3)))
b=np.matrix(np.random.randint(5,20,size=(3,3)))
c= np.matrix(np.ones((3,10)))
d=np.matrix(np.ones((3,10)))
print(a,b)
print(c,d)
print(np.array_equal(a,b))
print(np.array_less_equal(a,b))
print(np.array_equal(c,d))'''
'''print(np.identity(3))''' #solution 16
## NUMPY ARRAY MATHS

'''a = np.arange(2,11).reshape(3,3)
print(a)''' #solution 1

'''a = np.zeros(10)
print(a)
a[5]=11
print(a)''' #solution 2

'''a =np.arange(12,39)
print(a)''' #solution 3

'''a = np.arange(1,30)
print(a)
print(np.flip(a))''' #solution 3
'''a = np.arange(1,5)
print(a)
print(a.astype(float))''' #solution 4


'''arr = np.ones(shape=(5,5))
print(arr)
arr[1:4,1:4]=5
print(arr)''' #Solution no 6

'''arr = np.ones(shape=(5,5))
print(arr)
arr = np.pad(arr, pad_width=1,mode = 'constant',constant_values=0)
print(arr)''' #solution No 7

arr = np.ones(shape=(8,8))
print(len(arr))
for i in range(len(arr)):
    print(arr[i])
    for j in range( len(arr[i])):
        if i%2==0 and j%2==0:
            arr[i][j]=0
        
print(arr)
