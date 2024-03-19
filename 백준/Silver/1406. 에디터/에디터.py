import sys
from collections import deque

input = sys.stdin.readline

cursor_left = list(input().strip())
cursor_right = deque([])


command_num = int(input())

for _ in range(command_num):
    command = input().split()
    if command[0] == "L":
        if cursor_left:
            cursor_right.appendleft(cursor_left.pop())
    elif command[0] == "D":
        if cursor_right:
            cursor_left.append(cursor_right.popleft())
    elif command[0] == "B":
        if cursor_left:
            cursor_left.pop()
    elif command[0] == "P":
        cursor_left.append(command[1])

print("".join(cursor_left) + "".join(cursor_right))
