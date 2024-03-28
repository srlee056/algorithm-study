import sys

n, x = map(int, sys.stdin.readline().split())

list = list(map(int, sys.stdin.readline().split()))

result = [ele for ele in list if ele <x]

print(' '.join(map(str, result)))