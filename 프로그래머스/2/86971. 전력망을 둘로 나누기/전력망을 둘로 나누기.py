from collections import deque
def solution(n, wires):
    p=1
    parent_nodes={1:0}
    child_nodes={}
    wire_deque=deque(wires)
    
    while wire_deque:
        v1,v2=wire_deque.popleft()
        
        if v1 in parent_nodes:
            p,c=v1,v2
        elif v2 in parent_nodes:
            p,c=v2,v1
        else: 
            wire_deque.append([v1, v2])
            continue
        
        parent_nodes[c]=p
        child_nodes[p]=child_nodes.get(p, [])
        child_nodes[p].append(c)
        
    #print(parent_nodes)
    #print(child_nodes)
    subnode_counts = {}
    
    p_nodes = deque(child_nodes.keys())
    for i in range(1, n+1):
        if i not in p_nodes:
            subnode_counts[i] = 1
    
    while p_nodes:
        p = p_nodes.popleft()
        
        if any(c not in subnode_counts for c in child_nodes[p]):
            p_nodes.append(p)
        else:
            subnode_counts[p] = sum([subnode_counts[c] for c in child_nodes[p]])+1
        
    #print(subnode_counts)
    
    min_diff = n
    for value in subnode_counts.values():
        min_diff = min(min_diff, abs(n-value*2))
    
    #print(min_diff)
                
    answer = min_diff
    return answer