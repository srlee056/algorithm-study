from collections import deque
def solution(priorities, location):
    loc_priority=priorities[location]
    count=0
    p_queue=deque(list(range(len(priorities))))
    p_count=deque(sorted(priorities, reverse=True))
    #print(p_count)
    while p_queue:
        ele=p_queue.popleft()
        cur_p=p_count[0]
        #print(ele,cur_p)
        if priorities[ele]==cur_p:
            if ele==location:
                break
            p_count.popleft()
        else:
            p_queue.append(ele)
    #print(p_queue)      

    
    answer = len(priorities)-len(p_queue)
    return answer