import sys

# read size of triangle

n = int(sys.stdin.readline())

# read lines of numbers in triangle
triangle = []
for _ in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    triangle.append(line)

# started from second line of triangle,
# calculate max cumulative sum of current position
for i, line in enumerate(triangle[1:], 1):
    prev_line = triangle[i - 1]
    for j, num in enumerate(line):
        prev_left = prev_line[j - 1] if j > 0 else 0
        prev_right = prev_line[j] if j < len(prev_line) else 0
        line[j] += max(prev_left, prev_right)

print(max(triangle[-1]))
