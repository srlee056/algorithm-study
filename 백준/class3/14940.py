import sys

n, m = map(int, sys.stdin.readline().split())


regions = []

dest = [-1, -1]
for i in range(n):
    region_row = list(map(int, sys.stdin.readline().split()))
    if 2 in region_row:
        dest = [i, region_row.index(2)]
    regions.append(region_row)

dists = [[-1 if regions[i][j] else 0 for j in range(m)] for i in range(n)]


dest.append(0)
points = [dest]
visited = {}

for i in range(n):
    for j in range(m):
        visited[(i, j)] = False

d_x = [1, -1, 0, 0]
d_y = [0, 0, 1, -1]

while points:
    p_y, p_x, dist = points.pop(0)
    dists[p_y][p_x] = dist
    if visited[(p_y, p_x)]:
        continue
    else:
        visited[(p_y, p_x)] = True
    # print(p_y, p_x, dist)
    if dist == 0 and (p_y, p_x) != (dest[0], dest[1]):
        continue

    for i in range(4):
        new_x, new_y = p_x + d_x[i], p_y + d_y[i]
        if (new_x >= 0 and new_x < m) and (new_y >= 0 and new_y < n):
            if visited[(new_y, new_x)]:
                continue

            if regions[new_y][new_x] == 0:
                points.append([new_y, new_x, 0])
            else:
                points.append([new_y, new_x, dist + 1])


for d in dists:
    print(" ".join(map(str, d)))
