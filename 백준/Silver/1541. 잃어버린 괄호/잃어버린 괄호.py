from sys import stdin
from collections import deque

str = stdin.readline().strip()
str += "."
stack = deque()
number = ""

is_minus = False
result = [[], []]
for char in str:
    if char in ["+", "-", "."]:
        if is_minus:
            result[1].append(int(number))
        else:
            result[0].append(int(number))
        if char == "-":
            is_minus = True
        number = ""
    else:
        number += char

print(sum(result[0]) - sum(result[1]))
