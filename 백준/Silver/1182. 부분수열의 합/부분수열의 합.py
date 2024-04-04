import sys
from collections import deque

# sys.setrecursionlimit(10000000)
n, s = map(int, sys.stdin.readline().split())

numbers = list(map(int, sys.stdin.readline().split()))

n_queue = deque([])
for i, num in enumerate(numbers):
    n_queue.append((i, [num]))

count = 0
while n_queue:
    idx, nums = n_queue.popleft()

    if idx == n - 1:
        if sum(nums) == s:
            # print(idx, nums)
            count += 1
    else:
        idx += 1
        n_queue.append((idx, nums))
        n_queue.append((idx, nums + [numbers[idx]]))
        # print(n_queue)


print(count)
