def majorityElement(nums):
    candidate=0
    count=0

    for num in nums:
        if(count==0):
            candidate=num

        if num==candidate:
            count+=1
        else:
            count-=1
    return candidate

nums=[1,2,1,3,5,1,1]
print(majorityElement(nums))                