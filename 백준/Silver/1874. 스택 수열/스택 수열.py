import sys
from collections import deque
n = int(sys.stdin.readline())

cur_stack_pointer = 1
stack = deque([])
result = deque([])
for _ in range(n):
    result.append(int(sys.stdin.readline()))

prints = []
for i in range(1, n+1):
    stack.append(i)
    prints.append("+")
    while stack and result:
        stack_num = stack.pop()
        cur_num = result.popleft()
        if stack_num != cur_num:
            stack.append(stack_num)
            result.appendleft(cur_num)
            break
        else:
            prints.append("-")
            
if stack :
    print("NO")
else:
    for p in prints:
        print(p)