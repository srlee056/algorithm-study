import sys

n = int(input())

cases = [(sys.stdin.readline()) for i in range(n)]

for c in cases:
    scores = list(map(int, c.split()))
    stuNum = scores[0]
    stuAvg = sum(scores[1:])/stuNum
    count = 0
    for s in scores[1:]:
        if s > stuAvg : count += 1
    print("%.3f%%" %round(count/stuNum * 100, 3))

