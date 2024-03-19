import sys
from collections import deque


input = sys.stdin.readline

n = int(input())

for _ in range(n):
    input_list = list(input().strip())

    list_left_to_cursor, list_right_to_cursor = deque([]), deque([])
    for i in input_list:
        if i == "<":
            if list_left_to_cursor:
                temp_char = list_left_to_cursor.pop()
                list_right_to_cursor.appendleft(temp_char)
        elif i == ">":
            if list_right_to_cursor:
                temp_char = list_right_to_cursor.popleft()
                list_left_to_cursor.append(temp_char)
        elif i == "-":
            if list_left_to_cursor:
                list_left_to_cursor.pop()
        else:
            list_left_to_cursor.append(i)
        # print(list_left_to_cursor, list_right_to_cursor)
    print("".join(list_left_to_cursor + list_right_to_cursor))
