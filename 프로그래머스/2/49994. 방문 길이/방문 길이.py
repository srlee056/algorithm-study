def solution(dirs):
    answer = 0
    
    visited = {}
    for i in range(-5, 6):
        for j in range(-5, 6):
            visited[(i, j)] = []
    
    
    x, y = 0, 0
    dirD = {'U':[0, 1], 'D':[0, -1], 'L': [-1, 0], 'R':[1, 0]}
    oppdirD = {'U':'D', 'D':'U', 'L': 'R', 'R':'L'}
    count = 0
    for d in dirs:
        a, b = dirD[d]
        #print(x, y, d)
        if x+a in range(-5, 6) and y+b in range(-5, 6):
            #print(x, y, x+a, y+b, d)
            if d not in visited[x,y]:
                visited[(x, y)].append(d)
                visited[(x+a, y+b)].append(oppdirD[d])
                count += 1 
            x, y = x+a, y+b
    #print(count)
        
    return count