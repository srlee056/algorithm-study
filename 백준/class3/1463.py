import sys


def update_counts(v, value_with_counts, count):
    old_count = value_with_counts.get(v, count)
    value_with_counts[v] = min(old_count, count)


n = int(sys.stdin.readline())

value_with_counts = {n: 0}

while value_with_counts:
    v = max(value_with_counts)
    c = value_with_counts.pop(v)
    if v <= 1:
        print(c)
        break

    if v % 3 == 0:
        update_counts(v // 3, value_with_counts, c + 1)
    elif v % 3 == 1:
        update_counts((v - 1) // 3, value_with_counts, c + 2)
    else:
        update_counts((v - 2) // 3, value_with_counts, c + 3)

    if v % 2 == 0:
        update_counts(v // 2, value_with_counts, c + 1)
    else:
        update_counts((v - 1) // 2, value_with_counts, c + 2)
