from collections import Counter,OrderedDict,deque
from random import random


'''c = Counter({'a':4, 'b':5,'c':6})
for i in c.elements():
    print (i, end=' ')'''
'''s = str(input())
li = s.split(' ')
print(li)
c = Counter(li)
print(c)'''
'''de = deque([1,2,3])
for i in de:
    print(i)'''
'''s = str(input())
li = s.split(' ')
li2= []
for i in li:
    for j in i:
        li2.append(j)
c=Counter(li2)
for val,obj in c.items():
    if obj>1:
        print(val,'=',obj,end=' ')'''
'''s = str(input())
li = s.split(' ')
c = Counter(li)
count = 1
for i,j in c.items():
    if (j==1):
        print(i,end=' ')
        count=count+1
print('\n',count-1)'''

'''n = int(input())
od = OrderedDict()
sub_name = []
mark = []
for i in range(n):
    sub_marks = re.split(r'(\d+)$',input().strip())
    sub_name.append(sub_marks[0])
    mark.append(sub_marks[1])
    od[sub_name[i]]=int(mark[i])
for i,j in od.items():
    print(i,od[i])'''

'''de = deque([randint(10,30) for x in range(1,10)])
print(de)

de.pop()
de.popleft()
de.append(10)
de.appendleft(80)
x=9
print(de)
for k in range(len(de)):
    x=x-1
    print(de[x])'''
'''li = [randint(10,20) for x in range(1,10)]
de =deque(li)
print(de)'''
'''i = int(input("How many numbers do you want to add = "))
li = [randint(10,20) for x in range(1,10)]
de = deque(li)
for k in range(i):
    x = int(input())
    de.append(x)
print(de)
a = Counter(de)
print(a)'''
#key = int(input('Enter a specific number to check its count: '))
#if key in a:
    #print(a[key])
#else:
    #print('Key is not in the dict')

#for j in range(len(de)):
    #de.popleft()
#print(de)
#t = int(input("Input a number = "))
#for i in range(1,t+1):
    #de.rotate(i)
    #print(de)
'''nli = []
for i,j in a.items():
    nli.append(j)
k = max(nli)
f = 0
for t in a.keys():
    if k == a[t]:
        f = t
print(f,k,end='')'''
from heapq import*
'''li = [randint(1,10) for x in range (1,12)]
heapify(li)
print(li)
x=len(li)-1
n=len(li)-4
print('Do you want the smallest or largest 3 integers. Press 1 or 2: ')
inp = input()
li2 =[]
for i in range (x+1):
    if inp=='1':
     if (min(li)<=li[x] and i<=n):
        x = x - 1
        heappop(li)
        heapify(li)
     else:
         print(sorted(li))
         break
    else:
        if (min(li)<=li[x] and i<=2):
            x=x-1
            heappush(li2,min(li))
            heappop(li)
            heapify(li)
        else:
            print(sorted(li2))
            break'''
'''li =[randint(1,10) for x in range(10)]
li2 = []
n = len(li)-1
for i in range(n):
    heappush(li2,li[i])
print(li2)
for i in range(n):
    heapify(li2)
    print(heappop(li2),end='')
    if i<n-1:
       print(',',end='')
    else:
       print('.',end='')
print('\n',li2)'''
'''def litoheapli(li):
    heapify(li)
    return li
l = []
while True:
    x =input('Enter list elements. Double press enter to skip input = ')
    if x=='':
        break
    else:
        l.append(int(x))
x=litoheapli(l)
print(x)'''
'''x = [int(10*random()) for x in range(1,10)]
print(x)

while True:
    heapify(x)
    heappop(x)
    print(x)
    y=input()
    if y.isdigit():
      heappush(x,int(y))
      print(x)
    else:
        break'''
'''li = [int(10*random()) for x in range(1,11)]
n = len(li)
li2 = []
print(li)
for i in reversed(range(n)):
     heapify(li)
     li2.append(heappop(li))
print(li2)'''
'''li = [int(10*random()) for x in range(1,11)]
li2 = []
for i in range(len(li)):
    heapify(li)
    li2.append(heappop(li))
print(list(reversed(li2)))
k = int(input())
for i in reversed(range(len(li2))):
    if len(li2)-k==i:
        print('The kth(',k,')','largest number is = ', li2[i])
        break'''
'''product =1
li = [int(10*random()) for x in range(1,11)]
li2 = []
for i in range (len(li)):
    heapify(li)
    li2.append(heappop(li))
print(li2)

for i, k in enumerate(list(reversed(li2))):
   if i<3:
    product = product*k
    print(k)
   else:
       break
print(product)'''
'''li = [int(10*random()) for x in range(10)]
li2 =[]
for i in range(len(li)):
    heapify(li)
    li2.append(heappop(li))
print(li2)
for i in range(len(li2)):
    if li2.count(i)>1:
        print(li2[i],end='')
for i in range(len(li2)):        
    if li2.count(i)==1:
        print('\n',li2[i],end='')'''


'''li=[]
for x in range(5):
  l=dict()
  l["Name"]="Item"+str(x)
  l["Price"]=int(10*random())
  li.append(l)
print(li)
print(nsmallest(3,li,key=lambda x:x["Price"]))
print(nlargest(3,li,key=lambda x:x ["Price"]))'''
'''import timeit
setup=import random
h=
def statment():
    n,m = input().split(' ')
    li=[]
    for x in range(int(n)):
      for y in range(int(m)):
        li.append(int(10*random.random()))
    print(sorted(li))
    i = int(input())
    for index, x in enumerate(sorted(li)):
      if i-1==index:
        print(x)
        break
print(timeit.timeit(stmt=h,setup=setup,number=10000))'''

'''xy = lambda x,y: x*y
print(xy(5,2))
xx= lambda x : x+15
print(xx(5))'''
from random import*
'''x = lambda x: x*int(5*random())
print(x(5))'''
'''x= tuple((int(10*random()) for i in range(1,10)))
print(x)
y = lambda x: tuple(sorted(x))
print(y(x))'''
'''y=choice(range(5,10))
print(y)
dicton= lambda x:dict([(x,x**2) for x in range(y)])
l = list((map(dicton,[int(1*random()) for x in range(y)])))
print(l)
x = sorted(l,key=lambda x:x[2])
print(x)'''
'''x =list(y for x in list((int(10*random()),round(10*random(),2)) for i in range(10)) for y in x)
print(x)
FilterOut= filter(lambda a: True if a%2==0 else False,x)
print(list(FilterOut))'''
'''y=choice(range(2,3))
x = map(lambda x: x**y,list(int(10*random()) for i in range(10)))
print(list(x))'''
'''inp = str(input()).lower()
c = str(input())
start= lambda x: True if inp.startswith(c) else False
print(start(inp))'''
'''inp = str(input())
CheckNum = lambda x: True if inp.isdigit() else False
print(CheckNum(inp))'''
'''import math
r = range(int(input()))
fbSeries = list(map(lambda x: int((((1+math.sqrt(5))/2)**x-((1-math.sqrt(5))/2)**x)/math.sqrt(5)),[x for x in r]))
print(fbSeries)'''
'''from random import random
a= {int(10*random()) for x in range(10)}
b={int(10*random()) for x in range(10)}
common = lambda x,y: x.intersection(y)
print(common(a,b))'''
'''from random import random
a =[int(10*random()) for i in range(10)]
EvenCount= len(list(filter(lambda x: True if x%2==0 else False,a)))
OddCount = len(list(filter(lambda x: True if x%2!=0 else False,a)))
print(EvenCount,OddCount)'''
'''x = [int(100*random()) for i in range(20)]
fList= list(filter(lambda x: True if x%13==0 else(True if x%19==0 else False),x))
print(fList)'''
'''str = str(input())
palindrome = lambda x: True if str==str[::-1] else False
print(palindrome(str))'''
