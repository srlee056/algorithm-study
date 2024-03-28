import sys

distinct_nums = set()
for _ in range(10):
    num = int(sys.stdin.readline())
    distinct_nums.add(num%42)

print(len(distinct_nums))