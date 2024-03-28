from collections import defaultdict, deque
import copy
def solution(user_id, banned_id):
    
    
    matchings = defaultdict(set)
    
    for bid in banned_id:
        for uid in user_id:
            if is_matched(bid, uid):
                matchings[bid].add(uid)
    
    is_banned = {uid:False for uid in user_id}
    id_lists = recur_matching(deque(banned_id), matchings, is_banned)
    
    res = list(set(map(lambda i: tuple(sorted(i)), id_lists)))
    
    #print(res)
    
    return len(res)


def is_matched(bid, uid):
    if len(bid)!= len(uid):
        return False
    
    for i in range(len(bid)):
        if bid[i] != '*' and bid[i] != uid[i]:
            return False
    
    return True

def recur_matching(banned_id, matchings, is_banned):
    
    if len(banned_id) == 0:
        return [[]]
    
    bid = banned_id.popleft()
    candidates = matchings[bid]
    result = []
    #print(bid, candidates)
    #print(bid)
    for id in candidates:
        #print(id)
        if not is_banned[id]:
            is_banned[id] = True
            #print(result)
            temp = recur_matching(copy.deepcopy(banned_id), matchings, copy.deepcopy(is_banned))
            #print(temp)
            # if temp == [[]] : result.append([id])
            # else:   
            for t in temp:
                result.append([id]+t)
            #print(result)
            is_banned[id] = False
    
    return result