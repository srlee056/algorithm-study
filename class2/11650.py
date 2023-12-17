import sys


def quick_sort(points):
    if len(points) <= 1:
        return points

    pivot = points[0]
    tail = points[1:]

    lefts, rights = [], []
    for x in tail:
        if x[0] < pivot[0] or (x[0] == pivot[0] and x[1] < pivot[1]):
            lefts.append(x)
        elif x[0] > pivot[0] or (x[0] == pivot[0] and x[1] > pivot[1]):
            rights.append(x)

    return quick_sort(lefts) + [pivot] + quick_sort(rights)


n = int(sys.stdin.readline())

points = []
for _ in range(n):
    point = map(int, sys.stdin.readline().split())
    points.append(list(point))

# points.sort(key=lambda x: (x[0], x[1]))
points = quick_sort(points)
for point in points:
    print(f"{point[0]} {point[1]}")
