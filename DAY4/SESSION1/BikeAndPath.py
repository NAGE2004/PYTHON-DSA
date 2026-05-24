class RatRace:
    N=4
    def findPath(self,maze,row,col,path):
        if row==self.N-1 and col==self.N-1:#destination 
            print(path)
            return True
        if maze[row][col]==0 and row>=self.N and col>=self.N: #destination is 3,3 so check for 4,4 not to go --invalid path 
            return False
        
        maze[row][col]=0 #marking as viisted 
        
        #down operation
        if self.findPath(maze,row+1,col,path+"D"):
            return True
        
        #right operation 
        if self.findPath(maze,row,col+1,path+"R"):
            return True
        
        maze[row][col]=1 #revisited
        return False
maze=[[1,0,0,0],
    [1,1,0,1],
    [0,1,0,0],
    [1,1,1,1]]
obj=RatRace()
obj.findPath(maze,0,0,"")