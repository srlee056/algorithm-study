def solution(m, n, startX, startY, balls):
    
    # 원쿠션이기때문에 벽에 적어도 한번은 부딪혀야 함
    # 시작점의 공이 상하좌우의 벽 각각에 부딪혔을 때 그 거리의 제곱을 구하면 된다.
    # 입사/반사각이 같으므로, 벽 I에 대하여
    # 시작점 A, 종료 목표 B라고 하면
    # 벽I를 기준으로 B를 선대칭했을 때 점을 B'라고 한다면 원쿠션 거리는 
    # (A-B)x^2 + (A-B)y^2
    # A를 대칭했을때도 결과는 같음.
    
    aLeft = [-startX, startY]
    aRight = [2*m-startX, startY]
    aDown = [startX, -startY]
    aUp = [startX, 2*n-startY]
    
    #꼭짓점에 부딪히는 경우는 공 - 시작지점 - 꼭짓점이 같은 선에 있어야 가능하다.
    
    #이때 시작점과 목표의 x좌표가 같거나 y좌표가 같은건 원쿠션 조건에 영향을 주지 않는다.  
    minDists = []
    for b in balls:
        dist = (m+n)**2 
        isV = isVertex(startX, startY, b, m, n) #가능한지 여부와 그때의 진행거리 제곱
        if isV[0] : #꼭짓점에 원쿠션 가능한지 여부
            dist  = min(dist, isV[1]) 
        
        aList = [aUp, aDown, aLeft, aRight]
        if b[0] == startX : 
            if b[1] < startY : aList.pop(1) #aDown
            else : aList.pop(0) #aUp
        elif b[1] == startY : 
            if b[0] < startX : aList.pop(2) #aLeft
            else : aList.pop(3) #aRight
        #print(aList)
        for a in aList : 
            distAB = getDistance(a, b)
            dist = min(dist, distAB)
            
        minDists.append(dist)
    
    print(minDists)
    
    return minDists

def isVertex(aX, aY, b, m, n):
    #꼭짓점의 좌표는 다음과 같다.
    vx = [0, 0, m, m]
    vy = [0, n, 0, n]
    result = [False, 0]
    minDist = (m+n) ** 2
    for i in range(4) :
        if abs(b[0] - vx[i]) < abs(aX - vx[i]):
            continue
        by_ = (b[0] - vx[i]) * (aY - vy[i]) / (aX - vx[i])
        byR = (b[0] - vx[i]) * (aY - vy[i]) % (aX - vx[i])
        if (by_ == b[1] - vy[i]) and byR == 0 :
            aTmp = [2*vx[i] - aX, 2*vy[i] - aY]
            result = [True, min(minDist, getDistance(aTmp, b))]
            
    return result
    
def getDistance(a, b) :
    return (a[0]-b[0])**2 + (a[1]-b[1])**2