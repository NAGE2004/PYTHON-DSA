def mcCarthy91(n):
    if n>100:
        return n-10
    else:
        return mcCarthy91(mcCarthy91(n+11))
#main
n=int(input("Enter the number:"))

print(mcCarthy91(n))

