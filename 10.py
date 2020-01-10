class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
node=Node(1)
node2=Node(2,node)



class Linklist:
    def __init__(self):
        self.head=Node(None)
    def init_list(self,list_):
        p=self.head
        for x in list_:
            p.next=Node(x)

            p=p.next
    def show(self):
        p=self.head.next
        while p is not None:
            print(p.val)
            p=p.next
    def is_empty(self):
        if self.head.next is None:
            return True
        else:
            return False





l=Linklist()
l.init_list([2,4,5,6,6])
print(l.show())
print(l.is_empty())

class Stock(Exception):
    pass
class Sstack:
    def __init__(self):
        self.__elems=[]
    def is_empty(self):
        return self.__elems==[]
    def push(self,val):
        self.__elems.append(val)
    def pop(self):
        if self.is_empty():
            raise Stock
        return self.__elems.pop()
    def top(self):
        if self.is_empty():
            raise Stock
        return self.__elems[-1]
st=Sstack()
st.push(10)
st.push(20)
st.push(30)
while not st.is_empty():
    print(st.pop())







