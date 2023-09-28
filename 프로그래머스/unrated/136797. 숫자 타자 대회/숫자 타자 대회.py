from collections import deque

def solution(numbers):
    answer = 0
    
    # start from 5, any shortest route from 5 to 1~9 should pass number 5
    # and 0 has shortest path to 7, 8, 9. so from any number to 0 should pass one those three numbers.
    weights = initWeight()
    
    routeWeights = initRoute(weights, len(numbers))
    #print(weights)
    nums = [int(s) for s in numbers]
    answer = dp(nums, weights, routeWeights)
    
    #print(totalWeight)
    return answer

def initWeight():
    weights = [   #0, 1, 2, 3, 4, 5, 6, 7, 8, 9
        [1, 7, 6, 7, 5, 4, 5, 3, 2, 3],
        [7, 1, 2, 4, 2, 3, 5, 4, 5, 6],
        [6, 2, 1, 2, 3, 2, 3, 5, 4, 5],
        [7, 4, 2, 1, 5, 3, 2, 6, 5, 4],
        [5, 2, 3, 5, 1, 2, 4, 2, 3, 5],
        [4, 3, 2, 3, 2, 1, 2, 3, 2, 3],
        [5, 5, 3, 2, 4, 2, 1, 5, 3, 2],
        [3, 4, 5, 6, 2, 3, 5, 1, 2, 4],
        [2, 5, 4, 5, 3, 2, 3, 2, 1, 2],
        [3, 6, 5, 4, 5, 3, 2, 4, 2, 1]
    ]    
    return weights

def initRoute(weights, n):
    #routes = [[[[[0 for _ in range(10)] for _ in range(10)] for _ in range(10)] for _ in range(10)] for _ in range(n+1)]
    routes = [[[0 for _ in range(10)] for _ in range(10)] for _ in range(n+1)]
    #print(len(routes))
    #print(len(routes[n]))
    return routes

def dp (numbers, weights, routes):
    nLen = len(numbers)
    idxList = [(i, j) for i in range(10) for j in range(10)]
    prevLIdx = {4}
    prevRIdx = {6}
    for i in range(nLen):
        n = numbers[i]
        #print("start", i)
        for j in prevLIdx:
            for k in prevRIdx:
                if j == k: continue
                if i > 0 and routes[i][j][k] == 0: continue
                #print("jk - ",j, k)
                origV = routes[i+1][n][k]
                newV = routes[i][j][k] + weights[n][j] 
                routes[i+1][n][k] = newV if origV == 0 else min(origV, newV)
                #print(i, j, k ," to ", i+1, n, k, routes[i+1][n][k])
                
                origV = routes[i+1][j][n]
                newV = routes[i][j][k] + weights[n][k] 
                routes[i+1][j][n] = newV if origV == 0 else min(origV, newV)
                #print(i, j, k, " to ", i+1, j, n,  routes[i+1][j][n])
        prevLIdx.add(n)
        prevRIdx.add(n)
    
    result = -1
    for (i, j) in idxList:
        r = routes[nLen][i][j]
        if routes[nLen][i][j] > 0:
            if result == -1 : result = r
            else : result = min(result, r)
    #print(result)
    return result