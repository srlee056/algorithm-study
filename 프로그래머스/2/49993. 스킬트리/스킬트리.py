from collections import defaultdict

def solution(skill, skill_trees):

    count = 0
    for skill_tree in skill_trees:
        curr = 0
        hasAppeared = {k : False for k in skill}
        
        for s in skill_tree:
            if s in hasAppeared:
                
                hasAppeared[s] = True
            if curr < len(skill) and s == skill[curr]:
                curr += 1
        
        #print(hasAppeared)
        #print(curr, [k for k, x in hasAppeared.items() if x])
        if curr == len( [k for k, x in hasAppeared.items() if x]):
            
            count += 1
        
                
            
        
        
        
    return count
