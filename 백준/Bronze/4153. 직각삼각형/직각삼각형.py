import sys

isRightTriangle = []

while True :
    triangle = sys.stdin.readline().strip()
    a, b, c = map(int, triangle.split())
    if a == 0 and b == 0 and c == 0 :
        break
    else :
        tempMax = max(a, b, c)
        if tempMax == a :
            a = c
            c = tempMax
        elif tempMax == b:
            b = c
            c = tempMax
            
        if c * c == a * a + b * b :
            isRightTriangle.append('right')
        else :
            isRightTriangle.append('wrong')

for r in isRightTriangle:
    print(r)
