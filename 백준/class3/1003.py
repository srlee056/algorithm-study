import sys


# fib_print_zero = 1, 0, 1, 1, 2, ..
# fib_print_one = 0, 1, 1, 2, 3, ..
def fib_print(n):
    if n == 0:
        return [1, 0]
    elif n == 1:
        return [0, 1]
    else:
        n_1 = fib_print(n - 1)
        n_2 = fib_print(n - 2)
        return [n_1[0] + n_2[0], n_1[1] + n_2[1]]


test_cases = int(sys.stdin.readline())

for _ in range(test_cases):
    n = int(sys.stdin.readline())
    fib_prints = map(str, fib_print(n))
    print(" ".join(fib_prints))
