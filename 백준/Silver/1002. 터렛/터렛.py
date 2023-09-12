testCase = int(input())

for i in range(testCase):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    numOfPositions = 2

    #각각 x1, y1을 중심으로 하고 반지름이 r1인 원과, x2, y2를 중심으로 하고 반지름이 r2인 원의 접점을 찾는다
    #중심 사이의 거리를 구하고, 반지름과의 관계를 구한다.
    distSquare = (x2-x1)**2 + (y2-y1)**2
    if distSquare == 0 and r1 == r2: #same circle 
        numOfPositions = -1
    elif distSquare == (r1+r2)**2 or distSquare == (r2-r1)**2: #접점 한개 외접 or 내접
        numOfPositions = 1
    elif distSquare > (r1+r2)**2 or distSquare <(r2-r1)**2 : #점점 없음
        numOfPositions = 0


    print(numOfPositions)

