import sys
from collections import deque

n = int(sys.stdin.readline())

queue = deque()
for _ in range(n):
    commands = sys.stdin.readline().rstrip().split()

    if commands[0] == "push":
        queue.append(commands[1])
    elif commands[0] == "size":
        print(len(queue))
    elif commands[0] == "empty":
        if len(queue):
            print(0)
        else:
            print(1)
    else:
        if len(queue):
            if commands[0] == "pop":
                print(queue.popleft())
            elif commands[0] == "front":
                print(queue[0])
            elif commands[0] == "back":
                print(queue[-1])
        else:
            print(-1)
