#22. Write a Python program to print alphabet pattern 'M'.
from math import*
x= int(input())
for row in range (x+1):
 if row == int(ceil((x/2)-2)) :
     for col in range(1,x - 1):
         if col<(x-2)/2:
             print("*", end=' ')
         if col==ceil((x-2)/2):
             print(" ",end=" ")
         if col<x-1 and col>ceil((x-2)/2):
             print("*",end=" ")
 elif row== int(ceil((x/2)))-1:
     for col in range(1,x-1):
         if col ==1:
            print('*', end=' ')
         if col>1 and col<ceil((x-2)/2):
             print(' ',end=' ')
         if col==ceil((x-2)/2):
             print('*',end=' ')
         if col>ceil((x-2)/2) and col<x-2:
             print(' ',end=' ')
         if col ==x-2:
             print('*', end = ' ')



 else:
       for col in range(x-1):
           if col ==1:
               print('*',end=' ')
           if col == x-2:
               print('*',end=' ')
           if col>1 and col<x-2:
               print(' ',end=' ')




 print('\n')

'''if col>1 and col<ceil(x-2/2):    
             print(' ',end=' ')'''