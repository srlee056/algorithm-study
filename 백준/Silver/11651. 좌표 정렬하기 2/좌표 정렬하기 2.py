from sys import stdin

n = int(stdin.readline())

points = []

for _ in range(n):
    x, y = map(int, stdin.readline().split())
    points.append((y, x))

points_sorted = sorted(points)

for y, x in points_sorted:
    print(x, y)
