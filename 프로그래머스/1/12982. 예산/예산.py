def solution(d, budget):
    d.sort()
    i = 0
    while i < len(d):
        budget -= d[i]
        if budget >= 0 : 
            i += 1
        else :
            break
    return i