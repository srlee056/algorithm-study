import sys

n = int(sys.stdin.readline())

if n % 400 == 0 :
    answer = 1
elif n % 100 == 0 :
    answer = 0
elif n % 4 == 0:
    answer = 1
else : 
    answer = 0


print(answer)