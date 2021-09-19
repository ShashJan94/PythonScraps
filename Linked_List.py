'''class Node:
    def __init__(self,data):
        self.item=data
        self.ref=None

class LinkedList:
    def __init__(self):
        self.start_node = None

    def insertItem(self, data):
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node=new_node
class traverseList:
    def traseverseList(self):
        if self.start_node is None:
            print("List is Empty")
        else:
            n=self.start_node
            while n is not None:
                print(n.item)
                n=n.ref'''
class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class SinglyLinkList:
    def __init__(self):
        self.head=None
        self.tail= None
        self.count=0

    def iterateItems(self):
        currentitem=self.tail
        while currentitem:
            val=currentitem.data
            currentitem = currentitem.ref
            yield val
    def appenditem(self,data):
        node=Node(data)
        if self.head:
            self.head.ref=node
            self.head=node
        else:
            self.tail=node
            self.head=node
        self.count+=1

    def searchItem(self,data):
          if data in self.iterateItems():
              return True
          else:
              return False
    @property
    def returnsize(self):
        return print(self.count)
    def getItemByindex(self,index):
        self.i = index
        for ind,val in enumerate(list(self.iterateItems())):
            if self.i-1==ind:
                return print(val)
            else:
                return print("No Such index")
    def printlist(self):
        return print(list(self.iterateItems()))
    def popFirstElement(self):
        while self.iterateItems():
         if self.tail:
            self.tail=self.tail.ref
            break
         else:
            print("Nothing to pop")
            break
    def popLastElement(self):
        while self.iterateItems():
            if self.head:
             self.head.data=None
             break
            else:
                print("Nothing to Pop")
                break
    def deleteItemByVal(self,data):
        current=self.tail
        prev=self.tail
        while current:
            if current.data==data:
                if current == self.tail:
                    self.tail=current.ref
                else:
                    prev.ref=current.ref
                self.count=-1
                return
            prev=current
            current=current.ref
        
c=SinglyLinkList()
c.appenditem("hello")
c.appenditem("beta")
c.appenditem("Ghara")
c.appenditem("pop")
c.getItemByindex(1)
c.returnsize
c.popFirstElement()
c.popLastElement()
print(c.searchItem("cocl"))
print(list(c.iterateItems()))