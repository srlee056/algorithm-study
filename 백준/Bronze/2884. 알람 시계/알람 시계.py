import sys

H, M = map(int, sys.stdin.readline().split())

if M >= 45:
    M -= 45
else :
    H = (H-1) % 24
    M += 15
print(H, M)