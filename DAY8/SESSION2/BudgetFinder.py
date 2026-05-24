def budget_pair(prices,budget):
    left=0
    right=len(prices)-1

    while left<right:
        current_sum=prices[left]+prices[right]

        if current_sum==budget:
            return [prices[left],prices[right]]
        
        elif current_sum<budget:
            left+=1
        else:
            right=right+1
    return [-1.-1]

#Main

prices=[1,3,5,7,9]
budget=10
print(budget_pair(prices,budget))            