import sys

input = sys.stdin.readline

n = int(input().strip())

wh_list = []
for i in range(n):
    weight, height = map(int, input().split())
    wh_list.append((weight, height, i))

ranks = [1 for _ in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        w1, h1, i1 = wh_list[i]
        w2, h2, i2 = wh_list[j]
        if w1 < w2 and h1 < h2:
            ranks[i1] += 1
        elif w1 > w2 and h1 > h2:
            ranks[i2] += 1

print(" ".join(map(str, ranks)))
