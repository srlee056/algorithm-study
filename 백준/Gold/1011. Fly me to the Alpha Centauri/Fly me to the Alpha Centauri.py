import math

numCases = int(input())

for i in range(numCases):
    x, y = map(int, input().split())
    d = y-x
    ''' 수학적 규칙에 따라, 이동수가 n번이 되는 거리는 
        n = 2k-1 형태일 때 k*(k-1) <D <= k**2
        n = 2k 형태일 때 k**2 < D <= k*(k+1)
    '''

    # find k that k**2 <= D
    k = int(math.sqrt(d))
    if d == k**2:
        n = 2*k-1
    elif k**2 < d and d <= k*(k+1):
        n = 2*k
    else:
        n = 2*k + 1

    print(n)
