class Node:
    def __init__(self):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insert(self,data):
        newNode=Node(data)
        #Making the first node as head
        if self.head is None:
            self.head=newNode
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=newNode

    #Logic for removing duplicates
        def removeDupes(self):
            seen=set()
            temp=self.head
            prev=None

            while temp:
                if temp.data in seen:
                    prev.next=temp.next
                else:
                    seen.add(temp.data)
                    prev=temp
                temp=temp.next

        def display(self):
            temp=self.head
            while temp:
                print(temp.data,end="")
                temp=temp.next

#Input section
ids=list(map(int,input('enter the patients id:')))
sll=LinkedList
for x in s:
    sll.insert(x)

sll.removeduplicates()
print('unique ids are:')
sll.display()    





