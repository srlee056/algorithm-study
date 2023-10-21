def solution(s):
    answer = True
    openCount = 0
    for p in s :
        if p == '(' : openCount += 1
        elif p == ')' : openCount -= 1
        if openCount < 0 :
            return False
        
    if openCount != 0:
        return False
    
    return True