import sys

n = int(sys.stdin.readline())


num_dict = {}
for _ in range(n):
    m = int(sys.stdin.readline())
    num_dict[m] = num_dict.get(m, 0) + 1


for i in range(1, 10001):
    if i in num_dict:
        for _ in range(num_dict[i]):
            print(i)
