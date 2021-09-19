'''class Circle:
    def getArea(self,radius):
        self.radius = radius
        return 3.1416*(self.radius**2)
    def getCircumference(self,radius):
        self.radius=radius
        return 2*3.1416*self.radius

circle1 = Circle()
print(circle1.getArea(5),circle1.getCircumference(8))'''
from time import time, ctime

'''class Student:
    marks: int

    def __init__(self, age=0, marks=0):
        self.age, self.marks = age, marks

    def Display(self, name, surname, roll):
        self.name = name
        self.surname = surname
        self.roll = roll
        return [self.name,self.surname,self.roll,self.age,self.marks]

    def setAge(self, x):
        self.age = x

    def setMarks(self, x):
        self.marks = x
st1 = Student()
st1.setAge(20)
st1.setMarks(50)
print(st1.Display("Shashwata","Chowdhury",1234))'''
'''from datetime import*
from time import time,ctime
class Time:
       def addTime(self,time1,time2):
                self.time1 = time1
                self.time2 = time2
                s1,s2=list(map(int,time1.split(':'))),list(map(int,time2.split(':')))
                totalsec=0
                for i,j in zip(s1,s2):
                    if i==s1.__getitem__(0) and j==s2.__getitem__(0):
                        sec1=(j*60*60)+(i*60*60)
                    else:
                        sec2=(i*60)+(j*60)
                totalsec=sec1+sec2
                ntime=timedelta(seconds=totalsec)
                return ntime
       def displayCurrentTime(self):
           t=ctime()
           return t

       def displayMins(self,time1):
                self.time1=time1
                s1=list(map(int,time1.split(":")))
                for i in s1:
                    if i==s1.__getitem__(0):
                        totalmin=i*60
                    else:
                        totalmin=totalmin+i
                return str(totalmin)+" mins"
t1= Time()
print(t1.addTime("2:50","2:40"))
print(t1.displayMins("1:50"))
print(t1.displayCurrentTime())'''
'''class precedentValidation:
    def __init__(self,raw):
        self.raw=raw
        print(self.check(self.raw))

    def check(self, element):
        parenthesis=""
        str,stack=[], ["{","}","(",")","{","}"]
        self.element=element
        for paranthesis in self.element:
            if paranthesis in stack:
                str.append(paranthesis)
        for i in range(len(str)):
            if str[i]==stack[0] and str[i+1]==stack[1]:
                    return True
            elif str[i]==stack[2] and str[i+1]==stack[3]:
                    return True
            elif str[i]==stack[4] and str[i+1]==stack[5]:
                    return True
            else:
                    return False
ch_str1= precedentValidation("(Hello}")'''
'''class BracketValidation:
    stack = ["(", ")", "[", "]", "{", "}"]
    stack2 = ["()","{}","[]"]
    def __init__(self,str):
       self.str=str
       self.getBrackets(self.str)

    def getBrackets(self, string):
        self.string=string
        str=[]
        for paranthesis in self.string:
            if paranthesis in self.stack:
                str.append(paranthesis)
        print(str)
        print(self.checkBrackets(str))

    def checkBrackets(self,str1):
        self.str1=str1
        self.str2=''
        self.count=0
        for i in range(0,len(str1),2):
           if i<=len(self.str1):
            self.count = self.count + 1
            str2=str(self.str1[i]+self.str[i+1])
            if str2 in self.stack2:
                self.count=self.count+1
            else:
                return False
           else:
             break
        if self.count==len(str1) :
            return True
        else:
            return False


hello = BracketValidation("[]{}{}()")'''
from random import random

'''class Subset:
    def getSubset(self,list):
        self.list=list
        for i in range(len(self.list)+1):
            from itertools import combinations
            yield from combinations(self.list,i)

h= Subset()
li = [list(i) for i in h.getSubset([4,5,6])]
print(li)'''  # Need to figure out alternative
'''class SumElement:
    def getPairs(self,list,target):
        self.list=list
        for i in range(len(self.list)):
            if list[i-1]+list[i]==target:
                return print(i,",",i+1)
c=SumElement()
c.getPairs([10,20,10,40,50,60],50)'''
'''class Pow:
    def GetNumPower(self,x,y):
        return print(x**y)

d=Pow()
d.GetNumPower(2,3)'''

'''class ReverseString:
    def ReverseString(self,x):
        self.x=x
        k=''.join(sorted(list(x),reverse=True))#Letter By Letter
        l=self.x.split(" ")
        print(k, ' '.join(reversed(l))) #Word By Word
c=ReverseString()
c.ReverseString("Hello .py")'''
'''class PrintUpperCase:
    def get_string(self, x):
        self.x = x

    @property
    def print_string(self):
        return print(self.x.upper())
c = PrintUpperCase()
c.get_string('hi')
c.print_string'''
'''class Rectangle:
    def __init__(self,x,y):
        self.x,self.y=x,y
    @property
    def print_area(self):
        return print(self.x*self.y)
c=Rectangle(20,100)
c.print_area'''

