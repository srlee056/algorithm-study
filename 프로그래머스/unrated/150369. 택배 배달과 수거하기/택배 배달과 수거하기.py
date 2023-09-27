def solution(cap, n, deliveries, pickups):
    
    goDel, comePick = deliveries, pickups
    distance = 0
    
    goDist, comeDist = 0, 0
    for i in range(n-1, -1, -1):
        if goDel[i] > 0: 
            goDist = i+1
            break
            
    for i in range(n-1, -1, -1):
        if comePick[i] > 0: 
            comeDist = i+1
            break
    
    while True:
        distance += max(goDist, comeDist)*2
        capTemp = cap
        goTemp = goDist-1
        for i in range(goTemp, -1, -1):
            if goDel[i] > capTemp:
                goDel[i] -= capTemp
                break
            else :
                goDist = i 
                capTemp -= goDel[i]
                goDel[i] = 0
            
        capTemp = cap
        comeTemp = comeDist-1
        for i in range(comeTemp, -1, -1):
            if comeDist < i :
                continue
            if comePick[i] > capTemp:
                comePick[i] -= capTemp
                break
            else :
                comeDist = i
                capTemp -= comePick[i]
                comePick[i]  = 0
        
        if goDist <= 0 and comeDist <= 0:
            break
                
    return distance