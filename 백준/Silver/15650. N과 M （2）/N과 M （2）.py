import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# n C m
backtrack_dict = {}

for i in range(1, n + 1):
    backtrack_dict[(i, 1)] = [[j] for j in range(1, i + 1)]


def backtrack(n, m):
    result = []
    if (n, m) in backtrack_dict:
        return backtrack_dict[(n, m)]

    if n > 0 and m > 0:
        for i in range(1, n):
            if (n - i, m - 1) not in backtrack_dict:
                backtrack_dict[(n - i, m - 1)] = backtrack(n - i, m - 1)
            for back in backtrack_dict[(n - i, m - 1)]:
                arr = [i] + list(map(lambda x: x + i, back))
                result.append(arr)
        backtrack_dict[(n, m)] = result
    return result


arr = backtrack(n, m)
for a in arr:
    print(" ".join(map(str, a)))
