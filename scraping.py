'''from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
try:
 html =urlopen ("http://www.pythonscraping.com/exercises/exercise1.html").read()
except HTTPError as e:
    print(e)
else:
    print(html)'''

'''sum = int(input())
n = int(input())
result=0
total1,total2=0,0
x=1
for y in range(1,n+1):
    if x%2!=0:
        if y%2!=0:
          result =sum**x
          total1=total1+result
          print(result)

        else:
            result=-1*(sum**x)
            print(result)
            total2 = total2+result

    x = x + 2
print(total1+total2)'''

'''n = int(input())

for x in range(1,n+1):
    for y in range(1,n-x+2):
        print(' ',end='')
    for z in range (0,x+(x-1)):

        print('*',end='')
    print('\n')
for i in range(1,n+1):
    for j in range(1,i+2):
        print(' ',end='')
    for k  in range(0,(n-i)*2-1):
        print('*',end='')
    print('\n')'''
'''decimal = int(input())
divisor =2
t = decimal
while True:
 t = t/divisor
 if int(t)%2 == 0
     print(1, end='')
 else:
     print(0,end='')'''

'''x = int(input())
sum, result = 0,0
n = int(input())
factorial = 1
y=0
for k in range (1,(n*2)-1):
    factorial = factorial*k
    print(factorial)
    for i in range(1,1):
      result = result + ((-1**(y-1))*(x**((y*2)-2)/factorial)'''

'''from math import*
n = int(input())
x=2
for row in range(n+1):
    if(row<=int(ceil(n/2))):
        for col in range(row):
            print('*',end='')
    else:

        for col in range(int(ceil(n/2)+1-x)):
            print('*',end='')
        x=x+1
    print('\n')'''
'''from math import*
sum =((((1+sqrt(5))/2)**1-(((1-sqrt(5))/2)**1)))/sqrt(5)
n = int(input())
pow=2
for pow in range(n):
    sum = sum+((((1+sqrt(5))/2)**pow-(((1-sqrt(5))/2)**pow)))/sqrt(5)
    print(int(sum),',',end='')'''
'''from array import*
a = array('i',[])
b = array('i',[])
row = col = int(input())

for r in range(row):
    for c in range(col):
        a.insert(c,r*c)
        print(a[c],end='   ')
    print('\n')'''
'''text= []
while True:
    line = input()
    text.append(line)
    if line == '':
        break
for i in text:
    print(i.lower())'''

'''deci_in = int(input())
result = 0
count=0
di=deci_in*2
li=[]
for k in range(deci_in):
    di = int(di/2)
    if di>=1:
        count=count+1
        if di%2==0:
              li.append(0)
        else:
              li.append(1)
    else:
        break
for k in reversed(li):
    print(k,end='')'''


