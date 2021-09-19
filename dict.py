import string
from random import random
from typing import Dict, Any, Union
from collections import Counter

'''class DictSort:
    def __init__(self,dict):
      self.dict=dict
      print(self.sortdict(self.dict))

    def sortdict(self,dict):
        self.dict=dict
        l1=sorted(self.dict.items(),key=lambda item:item[1])
        l2=sorted(self.dict.items(),key=lambda item: item[1],reverse=True)
        return (l1,l2)
dict ={i:int(15*random()) for i in range(10)}
print(dict)
getLi= DictSort(dict)'''
'''class AddKey:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.dict={i:k*3 for i,k in enumerate(range(10))}
        print(self.dict)
        self.AddKey(self.dict,self.key,self.value)

    def AddKey(self,dict,key,value):
        self.key = key
        self.dict=dict
        self.value=value
        self.dict[self.key]=self.value
        return print(self.dict)

d1=AddKey(1,5)'''
'''class FindKey:
    dic={i:int(i*k*random()) for i,k in enumerate(range(11))}
    def CheckKey(self,key):
        print(self.dic)
        if key in self.dic:
            return True
        else:
            return False
key=FindKey()
print(key.CheckKey(10))'''
'''class IterateDic:
    dic = {i: int(i * k * random()) for i, k in enumerate(range(11))}
    def Iterate(self):
        for key,value in self.dic.items():
            print(key,":",value)
d=IterateDic()
d.Iterate()'''
'''class CreateDic:
    def dic(self,n):
        self.n=n
        self.d=lambda x: {i:i*i for i in range(1,x+1)}
        return print(self.d(self.n))
d = CreateDic()
d.dic(5)'''
'''class SquareDic:
    @property
    def GetDic(self):
     self.d= {i: i**2 for i in range(1,16)}
     return print(self.d)

d= SquareDic()
d.GetDic'''
'''class SumDic:
    @property
    def SumDic(self):
        self.d = {i: i ** 2 for i in range(1, 16)}
        print(self.d)
        return print(sum(self.d.values()))
d=SumDic()
d.SumDic'''
'''class RemoveKey:
    d = {i: i ** 2 for i in range(1, 16)}

    def removekey(self,key):
        self.key = key
        if self.key in self.d:
            del self.d[self.key]
            return print(self.d)
        else:
            return print("No Such Key")

d=RemoveKey()
d.removekey(32)'''
'''class MapList:
    def joinTwoListtoDic(self,key,value):
       self.li1,self.li2=key,value
       return print(zip(self.li1,self.li2))
key=[]
value=[]'''
'''class SortDic:
    def SortByKey(self,dic):
        self.dic=dic
        return print(sorted(dic))'''
'''class MaxMin:
    @property
    def GetMaxMin(self):
        self.d = {i: i ** 2 for i in range(1, 16)}
        return min(self.d.values()),max(self.d.values())'''
'''class Duplicate:
      d={i:int(i*random()) for i in range(0,10)}
      @property
      def removeDupicate(self):
          from collections import Counter
          print(self.d)
          self.c=Counter(self.d.values())
          for self.key,self.value in self.c.items():
                  if self.value>1:
                      self.c[self.key]=1
          self.nd={i:k for i,k in enumerate(self.c.keys())}
          return print(self.nd) #Random Key assignment


k=Duplicate()
k.removeDupicate'''
'''class DuplicateRemoval:
    @property
    def removeDupicate(self):
        self.d={i:int(10*random()) for i in range(1,10)}
        self.res=dict()
        print(self.d)
        for self.key,self.value in self.d.items():
            if self.value not in self.res.values():
                self.res[self.key]=self.value

        return print(self.res)
d=DuplicateRemoval()
d.removeDupicate'''
'''class DuplicateRemoval:
    @property
    def removeDuplicate(self):
        self.d={i:int(10*random()) for i in range(1,10)}
        print(self.d)
        self.keylist=list(self.d.keys())
        self.li1=[]
        i=0
        self.listof=list(dict.fromkeys(list(self.d.values())))





h=DuplicateRemoval()
h.removeDuplicate #Third method for number indexing'''
'''from string import*
from random import random
class AddDict:
    @property
    def mergeDict(self):
        self.r=range(1,20)
        self.d1={char:int(1000*random()) for char in ascii_lowercase}
        print(self.d1)
        self.d2={char:int(1000*random()) for char in ascii_lowercase}
        print(self.d2)
        from collections import Counter
        self.d3= Counter(self.d1)+Counter(self.d2)
        return print('\n',dict(self.d3))
d=AddDict()
d.mergeDict'''
'''class KthHighestValue:
    def __init__(self, r):
        self.GetKthHighestValue(r)

    def GetKthHighestValue(self, t):
        self.d = {i: int(20 * random()) for i in range(1, 11)}
        print(self.d)
        for self.i, self.k in enumerate(sorted(self.d.values(), reverse=True)):
            if t == self.i:
                break
            else:
                print(self.k)


d = KthHighestValue(3)'''
'''dict ="w3resource"
class StringToDict:
 def getStringtoDict(self,d):
   self.dict=d
   self.d={}
   letter: object
   for letter in self.dict:
    self.d[letter]=self.d.get(letter,0)+1
   print(self.d)
d=StringToDict()
d.getStringtoDict(dict)'''
'''class StringConcat:
    @property
    def dictConcat(self):
      dict={1:['a','b'],2:['c','d']}
      n=len(dict)
      for a in dict.get(n-1):
            for i in dict.get(n):
                print(a+i)'''
'''class CountValue:
    @property
    def CountValue(self):
        self.count=0
        self.dict=[{'id':1,'success':True,'name':'Larry'},{'id':2,'success':True,'name':"Pan"},{'id':3,'success':True,'name':"Len"}]
        for self.d in self.dict:
            for self.key,self.value in self.d.items():
                if self.value==True:
                    self.count=self.count+1
                else:
                    break
        return print(self.count)
d=CountValue()
d.CountValue'''
'''class GetShopItems:
    @property
    def GetShopItems(self):
        self.dict = {f'Item{i + 1}': round(uniform(20.40, 50.50), 2) for i in range(10)}
        print(self.dict)
        self.get_item_no = int(input())
        for self.index,self.item in zip(range(len(self.dict)),self.dict.items()):
            if self.index==self.get_item_no:
              break
            else:
                print(self.item,",",end="")
    

h = GetShopItems()
h.GetShopItems'''
from random import uniform
'''class GetTopItems:
    @property
    def GetTopItems(self):
        d={f'item{i+1}':round(uniform(40.50,70.20),2) for i in range(15)}
        d1=sorted(d.items(),key=lambda item:item[1]) #Easiest Way to Sort a Dict
        print(d1)
        count=0
        r1=int(input())
        for key in reversed(d1):
            count=count+1
            print(key)
            if count==r1:
                break
d=GetTopItems()
d.GetTopItems'''
'''class SortByValue:
     @property
     def SortByValue(self):
       self.d= {'Math': 81, 'Physics': 83, 'Chemistry': 87}
       print(Counter(self.d))
d= SortByValue()
d.SortByValue'''
'''class ReplaceValueBySum:
    d0: Dict[Any, Union[int, Any]]

    @property
    def ReplaceValue(self):
        self.d = {i: int(20 * random()) for i in range(1, 11)}
        self.d0={}
        for key,value in self.d.items():
            self.d0[key]=sum(self.d.values())
        print(self.d0)

h=ReplaceValueBySum()
h.ReplaceValue'''
'''class FindKeyMatch:
    @property

    def CheckKeyinDictionaries(self):
        get_key = str(input())
        dic1={f'key{i+1}':int(30*random()) for i in range(10)}
        dic2={f'key{i+1}':int(30*random()) for i in range(12)}
        if get_key.lower() in (dic1.keys() and dic2.keys()):
            return True
        else:
            return False

c=FindKeyMatch()
print(c.CheckKeyinDictionaries)'''
'''class AccessFifth:
 h={'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
    'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
'    z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
 for key,value in h.items():
          print(value[4])
d=AccessFifth()'''
'''class RemoveEmpty:
    dict={'c1': 'Red', 'c2': 'Green', 'c3': None}
    key1: str
    for key,val in dict.items():
        if val==None:
            key1=key
    del dict[key1]
    print(dict)
c=RemoveEmpty()'''
