class Node:
    self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insertAtend(self,data):
        newNode=Node(data)    

        if self.head is None:
            self.head=newNode
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=newNode

    def reverse(self):
        pre=None
        curr=self.head

        while curr:
            next=curr.next
            curr.next=pre
            pre=curr
            curr=next        
        self.head=pre    

def swap_nodes(self,x,y):

    if x==y:
        return
    
    preX=None
    preY=None
    currX=self.head
    currY=self.head
#Find X
    while currX and currX.data!=x:
        preX=currX
        currX=currX.next
#Find Y 
    while currY and currY.data!=y:
        preX=currX
        currY=currY.next

#Swap
    if not currX or not currY:
        return
    if preX:
        pre.next=currY

n=int(input("Enter the number:"))
list=list(map(int(int,input("enter the n values".split()))))
a,b=map(int,input("enter two values with spaces:").split())

sll=LinkedList()

for i in list:
    sll.__init__
    



    