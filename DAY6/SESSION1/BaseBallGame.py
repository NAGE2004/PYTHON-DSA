def baseBallGame(game):
    stack=[]
    for value in game:

        if value=="+":
            sum=value[-1]+game[-2]
            stack.append(sum)
        elif value=="D":
            stack=2*stack[-1]
            stack.append(sum)    
        elif value=="C":
            stack.pop()   
        else:
            stack.append(int(value))   
    return stack
         
gamelist=["5","2","C","D","+"]
totalStackSum=int(sum)