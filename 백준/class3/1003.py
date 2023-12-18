import sys


# fib_print_zero = 1, 0, 1, 1, 2, ..
# fib_print_one = 0, 1, 1, 2, 3, ..
def fib_print(n):
    for i in range(2, n + 1):
        if i not in fib_prints:
            fib_prints[i] = [fib_prints[i - 1][1], sum(fib_prints[i - 1])]


test_cases = int(sys.stdin.readline())

fib_prints = {0: [1, 0], 1: [0, 1]}

for _ in range(test_cases):
    n = int(sys.stdin.readline())
    fib_print(n)
    print(" ".join(map(str, fib_prints[n])))
