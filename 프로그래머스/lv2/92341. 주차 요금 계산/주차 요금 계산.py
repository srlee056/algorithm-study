def solution(fees, records):
    
    feesOfCarNum = {}
    timeCarIn = {}
    totalTimeGap = {}
    for r in records:
        t, carnum, inout = r.split()
        h, m = map(int, t.split(':'))
        if inout == 'IN':
            timeCarIn[carnum] = h*60 + m
        else: # inout == 'OUT'
            totalTimeGap[carnum] = totalTimeGap.get(carnum, 0) + h*60 + m - timeCarIn.pop(carnum)
            
    lastTime = 23*60 + 59
    for carnum, time in timeCarIn.items():
        totalTimeGap[carnum] = totalTimeGap.get(carnum, 0) + lastTime - time
    
    for carnum, timeGap in totalTimeGap.items():
        feesOfCarNum[carnum] = totalFee(fees, timeGap)
    
    #print(feesOfCarNum)
    answer = [v for k, v in sorted(feesOfCarNum.items())]
    #print(answer)
    return answer

def totalFee(fees, time):
    tFee = fees[1]
    
    if time > fees[0] :
        q = (time - fees[0]-1) // fees[2] + 1
        tFee += q * fees[3]
        
    return tFee