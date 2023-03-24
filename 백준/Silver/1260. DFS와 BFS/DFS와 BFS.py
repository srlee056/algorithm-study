'''
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
'''
from collections import defaultdict

def dfs(nodeLines, v, visited):
    
    nextNodes = nodeLines[v]
    visited.append(v)
     
    for n in nextNodes:
        if n not in visited:
            dfs(nodeLines, n, visited)
            
    return visited

def bfs(nodeLines, v):
    
    visited = []
    nodes = [v]
    while nodes:
        curNode = nodes.pop(0)
        if curNode not in visited:
            visited.append(curNode)
            nodes += nodeLines[curNode]

    return visited



if __name__ == "__main__":
    n, m, v = map(int, input().split())

    #default value가 list인 dictionay를 선언해준다.
    nodeLines = defaultdict(list)
    for i in range(m):
        sNode, eNode = map(int, input().split())
        
        #양방향 line이므로 각 node 모두 연결 node를 추가한다. 기본값이 []로 설정되어있으므로, 조건문을 따로 작성하지 않아도 된다.
        nodeLines[sNode].append(eNode)
        nodeLines[eNode].append(sNode)

    # 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하므로, sorting 진행
    for k in nodeLines.keys():
        nodeLines[k].sort()
    dfsList = dfs(nodeLines, v, [])
    print(' '.join(str(n) for n in dfsList))
    bfsList = bfs(nodeLines, v)
    print(' '.join(str(n) for n in bfsList))
