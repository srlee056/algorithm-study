import sys


def main():
    num, total_weight = map(int, sys.stdin.readline().split())

    elements = []
    for _ in range(num):
        weight, value = map(int, sys.stdin.readline().split())
        elements.append([weight, value])

    # 최대 무게 * 물건의 수

    value_by_weights_elements = [
        [0 for _ in range(total_weight + 1)] for _ in range(num + 1)
    ]

    for i, ele in enumerate(elements):
        for j in range(total_weight + 1):
            orig_val = value_by_weights_elements[i][j]
            if j >= ele[0]:
                new_val = value_by_weights_elements[i][j - ele[0]] + ele[1]
                value_by_weights_elements[i + 1][j] = max(orig_val, new_val)
            else:
                value_by_weights_elements[i + 1][j] = orig_val

    print(value_by_weights_elements[-1][-1])

if __name__ == "__main__":
    main()
