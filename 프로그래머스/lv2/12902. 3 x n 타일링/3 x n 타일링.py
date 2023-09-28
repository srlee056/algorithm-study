def solution(n):
    # there is 2 more way to fill 3 * n , which is similar to 3*4
    # | (--)(--) | 
    # | (--)(--) |
    # (--)(--)(--)
    
    m = n//2
    comb = [0] * (m+1)
    comb[1] = 3
    for i in range(2, m+1) :
        for j in range(1, i):
            if j == i-1 : mul = 3
            else : mul = 2
            comb[i] += comb[j] * mul
        comb[i] += 2
        #print(comb[i])
        
        comb[i] = comb[i] % 1000000007
    
    
    return comb[m]