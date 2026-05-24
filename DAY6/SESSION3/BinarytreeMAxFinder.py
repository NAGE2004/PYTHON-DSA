class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self):
        self.root=None
    def insertNode(self,data):
        self.root(None)    

    def insert(self,root,data):
        if root is None: 
            return Node(data)

        if data <root.data:
            root.left=self.insert(root.left,data)
        if data>root.data:
            root.right=self.insert(root.right,data)
        return root
    
# Finding of mAximum element in the tree
    def findthemaximum(self):
        if self.root is None:
            return None
    def findMax(self,root):
        if root is None:
            return
        leftMax=self.findMax(root.left)
        rightMax=self.findMax(root.right) 
        return max (root.data,leftMax,rightMax)

#MAIN
tree=BinaryTree
n=int(input("Enter the number of sections:"))

for i in range(n):
    value=int(input("Enter the values:"))
    

              
                       