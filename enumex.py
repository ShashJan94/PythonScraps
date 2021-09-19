import enum
from math import floor
from random import *

'''class DisplayEnumDataNameValue:
  class Country(enum.Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672
d=DisplayEnumDataNameValue()
print(d.Country.Albania)
for data in d.Country:
    print(data.name,data.value)'''
'''class DisplayEnumDataNameValue:
    class Country(enum.IntEnum):
        Afghanistan = 93
        Albania = 355
        Algeria = 213
        Andorra = 376
        Angola = 244
        Antarctica = 672

d = DisplayEnumDataNameValue()
for name in sorted(d.Country):
    print(name.name)'''
'''class DisplayEnumDataNameValue:
    class Country(enum.IntEnum):
        Afghanistan = 93
        Albania = 355
        Algeria = 213
        Andorra = 376
        Angola = 244
        Antarctica = 672

d = DisplayEnumDataNameValue()
print(list(map(int,d.Country)))'''
from collections import *

'''class DisplayEnumDataNameValue:
    class Country(enum.IntEnum):
        Pink=3
        Black=5
        White=6
        Red=1

d = DisplayEnumDataNameValue()
print(Counter(d.Country))'''

'''class CountStudent:
    classes = (
        ('V', 1),
        ('VI', 1),
        ('V', 2),
        ('VI', 2),
        ('VI', 3),
        ('VII', 1),
    )
    print(Counter(className for className,student in classes))'''
from array import array

'''class Array:
    arr=array('i',[10,20,30,40,50])
    for a in arr:
        print(a)'''
# Regular Method
'''class BinarySearch:
    def BinarySearch(self,l,t):
        print(l)
        check=lambda x: True if x in l else False
        print(check(t))
c=BinarySearch()
c.BinarySearch([i+1 for i in range(10)],6) #Easier Way'''
# Binary Method
'''class BinarySearch:
    def binary_search(self, arr: object, size: object, target: object) -> object:
        print(arr)
        left=0
        right=size-1
        found=False
        while left<=right:
            self.m=floor(left+right/2)
            if arr[self.m]<target:
                left=self.m+1
            elif arr[self.m]>target:
                right=self.m-1
            elif arr[self.m]==target:
                found=True
                return found
        return found

l=sorted(sample(range(1,20),10))
t=choice(range(1,10))
print(t)
c=BinarySearch()
print(c.binary_search(l,len(l),t))'''
'''class SequentialSearch:
    def seq_search(self,li,target):
        print(li," ",target)
        for i in li:
            if target==i:
                return True
        return False
a= [int(20*random()) for i in range(1,11)]
c= SequentialSearch()
f= choice(range(10))
print(c.seq_search(a,f))'''


'''class BubbleSort:
    @property
    def BubbleSort(self):
        li = sample(range(1,20),10)
        n= len(li)
        print(li)
        for i in range(n-1):
            for j in range(n-i-1):
                if li[j]>li[j+1]:
                    li[j],li[j+1]=li[j+1],li[j]
        return li
c = BubbleSort()
print(c.BubbleSort)'''

'''class BubbleSort:
    @property
    def BubbleSort(self):
        li=sample(range(1,20),10)
        print(li)
        n=len(li)
        for i in range(1,n):
            for j in range(1,n-i):
             if li[j-1]>li[j]:
                li[j-1],li[j]=li[j],li[j-1]
        return li
c=BubbleSort()
print(c.BubbleSort)'''

'''class SelectionSort:
    @property
    def SelectSort(self):
        li=sample(range(1,20),10)
        print(li)
        li2 = []
        le=len(li)
        for i in range(le):
            li2.append(min(li))
            li.remove(min(li))
        return li2
c = SelectionSort()
print(c.SelectSort)'''
#This still needs to be checked out



