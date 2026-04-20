def productException(num):
    n=len(num)
    result=[1]*n
    prefix=1
    for i in range(n):
        result[i]=prefix
        prefix*=num[i]
    suffix=1
    for i in range(n-1,-1,-1):
        result[i]=suffix
        suffix*=num[i]
    return result

num=[1,2,3,4]
print("productException:",productException(num))