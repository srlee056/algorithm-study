import sys

test_cases = int(sys.stdin.readline())
d_x = [0, 0, 1, -1]
d_y = [1, -1, 0, 0]

for _ in range(test_cases):
    m, n, k = map(int, sys.stdin.readline().split())
    points = []
    for _ in range(k):
        point = list(map(int, sys.stdin.readline().split()))
        points.append(point)

    count = 0
    orgin_points = points[:]
    while points:
        p = points.pop()
        neighbors = [p]
        count += 1
        while neighbors:
            nb = neighbors.pop()

            if nb not in points and nb != p:
                continue  # not crops
            elif nb in points:
                points.remove(nb)
            p_x, p_y = nb
            for i in range(4):
                if (p_x + d_x[i] >= 0 and p_x + d_x[i] < m) and (
                    p_y + d_y[i] >= 0 and p_y + d_y[i] < n
                ):
                    neighbors.append([p_x + d_x[i], p_y + d_y[i]])
        # print(points)
    print(count)
