from collections import deque

def solution(n):
    
    '''
    availables = [[0 for i in range(n)] for i in range(2*n-1)]
    
    for j in range(n):    
        availables[n-1-j][j] = 1
        availables[n-1][j] = 1
        availables[n-1+j][j] = 1
        availables[n-1-j][0] = 1
        availables[n-1+j][0] = 1
                
    for i in range(n):
        temp = availables[(n-1-i):(2*n-1-i)]
        print(i)
        for t in temp: print(t)
    '''
    
    choices = deque()
    for i in range(n):
        choices.append([[i], 0])
    
    count = 0
    while choices:
        choice, curIdx = choices.popleft()
        curIdx += 1
        
        if curIdx == n:
            count += 1
            #print(choice)
            continue
        
        if len(choice) != curIdx:
            print("error")
            break
        
        availables = dict.fromkeys(range(n), True)
        #print(availables)
        for i, c in enumerate(choice):
            availables[c] = False
            if c - (curIdx-i) >= 0 : availables[c - (curIdx-i)] = False
            if c + (curIdx-i) < n :availables[c + (curIdx-i)] = False
        
        for idx, val in availables.items():
            if val:
                choices.append([choice + [idx], curIdx])
        
    answer = 0
    return count