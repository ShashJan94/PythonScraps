'''inp= int(input())
with open('text.txt','r') as e:
    for index,line in enumerate(reversed((e.readlines()))):
        if inp!=index:
         print(line)
        else:
            break'''
'''x = []
with open('text.txt','r') as f:
    for line in f.readlines():
        x = x+line.split(' ')
print(max(x,key=len))'''
'''with open('text.txt','r') as f:
    cnt=-1
    while True:
        cnt+=1
        line =f.readline()
        if not line:
            break
        print(line)
print(cnt)'''
'''from collections import Counter
x = []
with open('text.txt','r') as f:
    for line in f.readlines():
        x = x+line.split(' ')
c = Counter(x)
print(c)'''
'''#text =(('Hi', 'steve', 'how', 'are', 'you'),('Not', 'bad', 'mate'))
text = (("Hi steve how are you"),('I am fine')) #You can write like above or you can write like the beside assignment
li = [word for sentence in text for word in sentence.split(' ')]
print(li)
with open('text.txt','a') as f:
    f.writelines(' '.join(li))
with open('text.txt','r') as f:
    print(f.read())'''
'''with open('text.txt','r') as f:
    with open('text1.txt','w+') as e:
        e.writelines(f.readlines())
with open('text1.txt','r') as f:
    print(f.read())'''
'''from random import choice
with open('text.txt','r') as f:
    r =choice(f.readlines())
    print(r)'''
'''with open('text.txt','r') as f:
    with open('text1.txt','r') as e:
        for line,line1 in zip(f.readlines(),e.readlines()):
            print(line+line1)'''
'''f = open('text1.txt','r')
if not f.close():
    print('file is not closed')
    f.close()
else:
    print('closed')'''
'''import re
with open('text1.txt','r') as f:
    cnt=0
    for line in f.readlines():
        for word in re.split('[ ,]',line):
            print(word)
            cnt+=1
print(cnt)'''

m =[1,2,3]
n=m
m.pop()
print(n)