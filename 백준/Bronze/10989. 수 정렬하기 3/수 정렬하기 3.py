import sys

n = int(sys.stdin.readline())


nums = [0 for _ in range(10001)]
for _ in range(n):
    m = int(sys.stdin.readline())
    nums[m] += 1


for i, num in enumerate(nums):
    for _ in range(num):
        print(i)
