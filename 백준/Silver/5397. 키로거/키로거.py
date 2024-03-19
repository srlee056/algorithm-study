import sys
from collections import deque


input = sys.stdin.readline

n = int(input())

for _ in range(n):
    input_list = list(input().strip())

    cursor_left, cursor_right = deque([]), deque([])
    for char in input_list:
        if char == "<":
            if cursor_left:
                cursor_right.appendleft(cursor_left.pop())
        elif char == ">":
            if cursor_right:
                cursor_left.append(cursor_right.popleft())
        elif char == "-":
            if cursor_left:
                cursor_left.pop()
        else:
            cursor_left.append(char)

    # 효율적인 문자열 합치기
    print("".join(cursor_left) + "".join(cursor_right))
