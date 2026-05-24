from queue import Queue

def avg(q):
    total=0
    n=q.size()
    temp=Queue()

    #sum
    while not q.empty():
        value=q.get()
        total+=value
        temp.put(value)
    while not temp.empty():
        q.put(temp.get())
    return total/n    


#INPUT

n=int(input("Enter the size"))    
q=Queue()

print("Enter the elements:")
elements=list(map(int,input().split()))

for i in range(n):
    q.put(elements[i])

avg=avg(q)
print("Average number of items:",avg)

