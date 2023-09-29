def solution(maps):
    n, m = len(maps), len(maps[0])
    islands = []
    
    newMaps = [list(s) for s in maps ]
    
    for i in range(n):
        for j in range(m):
            if newMaps[i][j] != 'X':
                #get island and total value of foods
                foods= 0
                points = {(i, j)}
                
                while points:
                    a, b = points.pop()
                    foods += int(newMaps[a][b])
                    newMaps[a][b] = 'X'
                    
                    #print(i, j, a, b)
                    moves = []
                    if b < m-1 : moves.append((a, b+1))
                    if b > 0 : moves.append((a, b-1))
                    if a < n-1 : moves.append((a+1, b))
                    if a > 0 : moves.append((a-1, b))
                    
                    for k, l in moves:
                        if newMaps[k][l] != 'X' : 
                            points.add((k, l))
                islands.append(foods)
                    
    #print(islands)
    if len(islands) == 0 : islands.append(-1)
    else : islands.sort()
    
    return islands