def solution(s):
    maxLen = 1
    for i in range(1, len(s)-1):
        #print("mid value", s[i])
        
        l = i-1
        r = i+1
        while l >=0 and r < len(s):
            if s[l] == s[r]:
                l -= 1
                r += 1
            else :
                break
        #print("odd", s[l+1:r])
        maxLen = max(maxLen, len(s[l+1:r]))
    
    for j in range(len(s)-1):
        #print("even length palindrom")

        l = j
        r = j+1
        while l >=0 and r < len(s):
            if s[l] == s[r]:
                l -= 1
                r += 1
            else :
                break
        #print("even", s[l+1:r])
        maxLen = max(maxLen, len(s[l+1:r]))    
        
    #print(maxLen)

    return maxLen