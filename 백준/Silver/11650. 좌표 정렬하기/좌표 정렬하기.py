import sys

n = int(sys.stdin.readline())

points = []
for _ in range(n):
    point = map(int, sys.stdin.readline().split())
    points.append(list(point))

points.sort(key=lambda x: (x[0], x[1]))
for point in points:
    print(f"{point[0]} {point[1]}")
