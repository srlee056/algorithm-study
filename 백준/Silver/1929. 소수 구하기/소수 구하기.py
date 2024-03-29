import sys

m, n = map(int, sys.stdin.readline().split())

prime_nums = [1 for _ in range(n+1)]

prime_nums[0], prime_nums[1] = 0, 0

for i in range(2, n+1):
    if prime_nums[i] == 1:
        for j in range(i*2, n+1, i):
            prime_nums[j] = 0

for k in range(m, n+1):
    if prime_nums[k] == 1:
        print(k)
