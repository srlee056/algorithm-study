import sys
sys.setrecursionlimit(100000)

def solution(triangle):
    
    
    while len(triangle) > 1:
        bottom = triangle.pop(-1)
        for i in range(len(bottom)-1):
            triangle[-1][i] += max(bottom[i], bottom[i+1])
        
    print(triangle)
        
    
    return triangle[0][0]

def dfs(triangle, triSum):
    if len(triangle) == 0:
        return 0
    if len(triangle) == 1:
        return triangle[0][0]
    
    root = triangle[0][0]
    leftTree, rightTree = [], []
    
    leftTree = [n[:-1] for n in triangle[1:]]
    rightTree = [n[1:] for n in triangle[1:]]
    
    leftValue = root + dfs(leftTree)
    rightValue = root + dfs(rightTree)
    
    #print(root, leftTree, rightTree)
    return max((leftValue, rightValue))