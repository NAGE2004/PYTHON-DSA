def thirdMax(nums):
    nums.sort()

    unique=[]
    unique.append(nums[0])

    for i in range(1,len(nums)):
        if nums[i]!=nums[i-1]:
            unique.append(nums[i])

    k=len(unique)

    if k<3:
        return unique[k-1]
  
    #low high
    low=0
    high=k-1
    target=k-3

    while low<=high:
        #mid=low+(high-low)/2
        mid=(low+high)//2
        if mid==target:
            return unique[mid]
        elif mid<target:
            low=mid+1
        else:
            high=mid-1
    return -1        

#Main

n=int(input("Enter the numbers: "))

nums=list(map(int,input("Enter the numbers:").split()))
nums=[1,3,2,2,3,4]
print("Answer:",thirdMax(nums))