def solution(n):

    fills = [0, 1, 2]
    
    for i in range(3, n+1):
        ff = (fills[i-1] + fills[i-2])% 1000000007
        fills.append(ff)
    
    #print(fills)
    
    return fills[n] 