n = int(input())

points = []
for _ in range(n):
    point = map(int, input().split())
    points.append(list(point))


points.sort(key=lambda x: (x[0], x[1]))
for point in points:
    print(f"{point[0]} {point[1]}")
