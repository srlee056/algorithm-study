import sys

k, n = map(int, input().split())
lines = [int(sys.stdin.readline().strip()) for _ in range(k)]

avg_ = sum(lines)//n

#print(avg_)
startNum, endNum = 1, avg_+1

while startNum < endNum-1:
    #print(startNum, endNum)
    length = (startNum+endNum)//2
    #print(length)
    sum_ = sum([l//length for l in lines])
    #print(sum_)
    if sum_ < n : endNum = length
    else : startNum = length

print(startNum)
