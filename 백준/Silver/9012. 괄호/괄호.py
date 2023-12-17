import sys

n = int(sys.stdin.readline())

for _ in range(n):
    paren_str = sys.stdin.readline().rstrip()

    valid = 0
    for p in paren_str:
        if p == "(":
            valid += 1
        elif p == ")":
            valid -= 1

        if valid < 0:
            break

    if valid == 0:
        print("YES")
    else:
        print("NO")
