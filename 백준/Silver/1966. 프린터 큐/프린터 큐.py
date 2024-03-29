import sys
from collections import deque
input = sys.stdin.readline

test_cases = int(input().strip())

for _ in range(test_cases):
    n, m = map(int, input().split())
    priorities = deque([(int(p),i ) for i, p in enumerate(input().split())])
    #print(priorities)
    sorted_prior = sorted([p for (p, i) in priorities])
    #print(sorted_prior)

    count = 1
    while sorted_prior:
        cur_prior = sorted_prior.pop()
        while priorities:
            prior, idx = priorities.popleft()
            #print(cur_prior)
            #print(prior, idx, m)
            if cur_prior==prior:
                if idx == m:
                    print(count)
                else:
                    count += 1
                break
            else:
                priorities.append((prior, idx))
