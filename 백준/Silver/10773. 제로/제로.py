import sys

k = int(sys.stdin.readline())


records = [0]
for _ in range(k):
    m = int(sys.stdin.readline())
    if m == 0:
        records.pop()
    else:
        records.append(m)


print(sum(records))
