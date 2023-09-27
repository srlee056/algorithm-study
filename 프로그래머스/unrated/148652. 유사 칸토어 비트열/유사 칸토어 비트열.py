def solution(n, l, r):
    # replace 1 to 11011, 0 to 00000
    # nth element, how many 1s in specific range
    # 5진수로 나타내면 어떨까?
    # 4 = 4(5), 17 = 32(5)
    # 1th element = 11011
    # 2th element -> from 04 to 32 => (11 11011 00000 11)
    lBit, rBit = [0] * n, [0] * n
    lOrig, rOrig = l, r
    for i in range(n-1, -1, -1) :
        lBit[i] = l % 5
        l = l // 5                 
        rBit[i] = r % 5
        r = r // 5
    
    #calculate 1s in 0 to i (idx) in nth element
    
    #print(countOnes(n, lOrig-1))
    #print(countOnes(n, rOrig))
    
    #print(lBit)
    #print(rBit)
    
    answer = countOnes(n, rOrig) - countOnes(n, lOrig-1)
    return answer

def countOnes(n, i):
    iBit = [0 for _ in range(n+1)]
    iOrig = i
    
    for j in range(n, -1, -1) :
        iBit[j] = i % 5
        i = i // 5
        
    mulList = [0, 1, 2, 2, 3]
    result = 0
    print(iOrig, iBit)
    for j in range(n+1) :
        result += mulList[iBit[j]] * (4**(n-j))
        print(j, result)
        if iBit[j] == 2 :
            break
        
    return result
    