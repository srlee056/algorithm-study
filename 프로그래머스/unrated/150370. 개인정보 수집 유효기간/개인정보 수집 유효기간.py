def solution(today, terms, privacies):
    
    #print(today)
    
    periods = {}
    for t in terms:
        name, period = t.split()
        print(name, period)
        periods[name] = int(period)
        
    #print(periods)
    
    expireds = []
    for i in range(len(privacies)):
        p = privacies[i]
        startDate, name = p.split()
       # print(startDate, name)
        if isExpired(startDate, today, periods[name]) :
            expireds.append(i+1)
        
    
    print(terms)
    print(privacies)
    
    return expireds

def isExpired(startDate, endDate, period):
    #stardDate와 endDate사이의 기간을 계산하고, period(유효기간) 정보가 주어졌을 때, 약관이 만료되었는지 확인하는 함수
    starts = list(map(int, startDate.split('.')))
    ends = list(map(int, endDate.split('.')))
    #print(starts, ends)
    
    # period가 6이라면, 5 months 27 dates를 더한 날과 endDate를 비교
    """
    periods = [0, period-1, 27]
    
    for i in range(3):
        starts[i] += periods[i]
    
    if starts[2] > 28 : 
        starts[2] -= 28
        starts[1] += 1
    if starts[1] > 12 :
        starts[1] -= 12
        starts[0] += 1
        
    print(starts, ends)
    """
    
    # 각 달이 28일로 동일하므로, 두 날짜의 차이를 단순 계산을 통해 n월 m일로 확인 가능.
    # a년 b월 c일 인 경우, (a * 12 + b) * 28 + c 로 계산하고 두 날짜의 차이를 계산한다.
    startDays = (starts[0] * 12 + starts[1]) * 28 + starts[2]
    endDays = (ends[0]*12 + ends[1])*28 + ends[2]
    
    diffDays = endDays-startDays
    periodDays = period*28
    
    #print(diffDays, periodDays)
    
    if diffDays < periodDays : # 만료되지 않음
        return False
    else : 
        return True
    
    