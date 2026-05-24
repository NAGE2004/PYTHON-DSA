def logisticsRoute(route):

    if not routes:
        print("Please Enter the values:")
        return
    shortest=routes[0][2]
    longest=routes[0][2]
    total=0
    city_connections={}
    for src,dest,distance in routes:
        if distance>longest:
            longest=distance
        total+=distance

        city_connections[src]=city_connections.get(src,0)+1
        city_connections[dest]=city_connections.get(dest,0)+1

    average=total/len(routes)
    above_avg=0

    for src,dest,distance in routes:
        if distance>average:
            above_avg+=1

        print("shortest",shortest)
        print("Lonegst",longest)
        print("Totla",total)
        print("Average",average)
        print("Above avg",above_avg)
        print("City Connections",city_connections)    

routes=[(0,1,10),(0,2,25),(1,2,15),(1,3,30),(2,3,20)]
print("TEST CASE 1")
logisticsRoute(routes)