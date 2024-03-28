import sys

input = sys.stdin.readline

A = int(input().strip())
B = int(input().strip())
C = int(input().strip())

mul = str(A * B * C)

counts = [0 for _ in range(10)]

for char in mul:
    counts[int(char)] += 1

for count in counts:
    print(count)