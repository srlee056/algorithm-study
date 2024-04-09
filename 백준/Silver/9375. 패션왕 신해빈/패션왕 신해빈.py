import sys
from collections import defaultdict


def main():
    cases = int(sys.stdin.readline().strip())

    for _ in range(cases):
        n = int(sys.stdin.readline().strip())
        clothes = defaultdict(list)
        for _ in range(n):
            name, type = sys.stdin.readline().split()
            clothes[type].append(name)

        mul = 1
        for k, v in clothes.items():
            mul = mul * (len(v) + 1)

        print(mul - 1)


if __name__ == "__main__":
    main()
