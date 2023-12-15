from collections import deque
import itertools


def main():
    num_of_tests = int(input())

    test_cases = []
    for i in range(num_of_tests):
        funcs = input()
        num_of_elements = int(input())
        elements = map(int, input()[1:-1].split(","))
        if num_of_elements != 0:
            elements = list(elements)
        else:
            elements = []
        test_cases.append((deque(funcs), num_of_elements, elements))

    for funcs, num_of_elements, elements in test_cases:
        left, right = 0, num_of_elements - 1
        is_reversed = False

        while funcs:
            func = funcs.popleft()

            if func == "R":
                is_reversed = not is_reversed

            elif func == "D":
                if is_reversed:
                    right -= 1
                else:
                    left += 1

        if left > right + 1:
            print("error")

        else:
            result = (
                list(reversed(elements[left : right + 1]))
                if is_reversed
                else elements[left : right + 1]
            )
            result = "[" + ",".join(map(str, result)) + "]"
            print(result)


if __name__ == "__main__":
    main()
