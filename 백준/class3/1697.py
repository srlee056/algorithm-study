import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

visited = {n: True}
position = deque([{n}])
count = 0
while position:
    cur_set = position.popleft()

    if k in cur_set:
        print(count)
        break
    else:
        next_set = set()
        for cur in cur_set:
            visited[cur] = True
            # 메모리 초과를 막기 위해 0, 100000 범위를 지정했더니 해결됨
            if (cur - 1) not in visited and cur - 1 >= 0:
                next_set.add(cur - 1)
            if (cur + 1) not in visited and cur + 1 <= 100000:
                next_set.add(cur + 1)
            if (cur * 2) not in visited and cur * 2 <= 100000:
                next_set.add(cur * 2)
        position.append(next_set)
        count += 1
