def solution(common):
    
    diff1 = common[1]- common[0]
    diff2 = common[2]- common[1]
    
    if diff1==diff2 : # 등차수열
        return common[-1] + diff1
    else : # 등비수열
        mul = common[1] // common[0]
        return common[-1] * mul
    