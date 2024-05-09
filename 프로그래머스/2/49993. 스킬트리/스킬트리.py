from collections import defaultdict

def solution(skill, skill_trees):

    count = 0
    
    for skill_tree in skill_trees:
        cur_idx = 0
        is_valid = True
        for skill_ in skill_tree:
            if skill_ in skill:
                if skill_ != skill[cur_idx]:
                    is_valid = False
                    break
                else:
                    cur_idx += 1
        if is_valid:
            count += 1
    return count
