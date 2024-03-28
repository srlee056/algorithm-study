import sys

list = map(int, sys.stdin.readline().split())

sum_of_nums = sum([num**2 for num in list])

print(sum_of_nums%10)