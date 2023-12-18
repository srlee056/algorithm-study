import sys

n = int(sys.stdin.readline())

value_with_counts = {n: 0}

while value_with_counts:
    v = max(value_with_counts)
    c = value_with_counts.pop(v)
    if v <= 1:
        print(c)
        break

    if v % 3 == 0:
        old_count = value_with_counts.get(v // 3, c + 1)
        value_with_counts[v // 3] = min(old_count, c + 1)
    elif v % 3 == 1:
        old_count = value_with_counts.get((v - 1) // 3, c + 2)
        value_with_counts[(v - 1) // 3] = min(old_count, c + 2)
    else:
        old_count = value_with_counts.get((v - 2) // 3, c + 3)
        value_with_counts[(v - 2) // 3] = min(old_count, c + 3)

    if v % 2 == 0:
        old_count = value_with_counts.get(v // 2, c + 1)
        value_with_counts[v // 2] = min(old_count, c + 1)
    else:
        old_count = value_with_counts.get((v - 1) // 2, c + 2)
        value_with_counts[(v - 1) // 2] = min(old_count, c + 2)

