from collections import deque

def solution(m, n, puddles):
    
    # 진행 방향은 오른쪽 , 아래 (x +1, y+1)
    # from x, y = 0, 0 to m, n
    # if next x, y in puddles : do not go
    
    routes = {(1,1):1}
    for i, j in puddles:
        routes[(i, j)] = 0
    
    for i in range(m+1):
        routes[(i, 0)] = 0
    for j in range(n+1):
        routes[(0, j)] = 0
    #print(routes)
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if (i, j) in routes :
                continue
            routes[(i,j)] = routes[(i, j-1)] + routes[(i-1, j)]

                    
    
    count = 0
    return routes[(m, n)] % 1000000007