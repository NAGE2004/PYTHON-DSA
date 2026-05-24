class TreeNode:
    def __init__(self,val=0):
        self.val=val
        self.left=None
        self.right=None

class solution:
    def buildTree(arr):
        if not arr or arr[0] is None:
            return None 
        root=TreeNode(arr[0]) 
        queue=[root]
        i=1
        while       



sample=[[3,2,3,None,3,None,1],
        [3,4,5,1,3,None,1],
        [5],
        [1,2,3],
        [4,1,None,2,None,3]]