import sys

n, k = map(int, sys.stdin.readline().split())

circle = [i for i in range(1, n + 1)]
removed = []
while len(circle):
    l = len(circle)
    k_idx = (k - 1) % l
    removed.append(circle[k_idx])

    if k_idx == l - 1:
        circle = circle[:k_idx]
    else:
        circle = circle[k_idx + 1 :] + circle[:k_idx]


print("<{}>".format(", ".join(map(str, removed))))
