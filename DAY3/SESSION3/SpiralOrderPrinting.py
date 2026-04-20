def SpiralOrder(matrix,m,n):
    top=0
    bottom=m-1
    left=0
    right=n-1

    while top<=bottom & left<=right:

        #first row
        for i in range(left,right+1):
            print(matrix[top][i],end=" ")
        top+=1   

        #right coloumn
        for i in range(top,bottom+1):
            print(matrix[i][right],end=" ")

        right-=1
        
        #Bottom row
        if top<=bottom:
            for i in range(right,left-1,-1):
                print(matrix[bottom][i],end=" ")
            bottom-=1

        if left<=right:
            for i in range(bottom,top,-1,-1):
                print(matrix[i],[left],endl=" ")
            left+=1                 

#main program
n=3
m=3

print("Enter your matrix:")
matrix=[[1,2,3],[4,5,6],[7,8,9]]
matrix=[tuple(map(int,input().split()))for _ in range(m)]
print(matrix)
print(SpiralOrder(matrix,m,n))
