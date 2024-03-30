import sys

A, B, V = map(int, sys.stdin.readline().split())

cur_height = 0
day = 1
if A < V :
    day += (V-A-1) // (A-B) + 1

print(day)