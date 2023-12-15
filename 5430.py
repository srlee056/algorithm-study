def process_elements(funcs, elements, is_reversed):
    left, right = 0, len(elements) - 1

    for func in funcs:
        if func == "R":
            is_reversed = not is_reversed
        elif func == "D":
            if is_reversed:
                right -= 1
            else:
                left += 1

    if left > right + 1:
        return "error"
    else:
        result = elements[left : right + 1]
        if is_reversed:
            result = result[::-1]

        return "[" + ",".join(map(str, result)) + "]"


def main():
    num_of_tests = int(input())

    for i in range(num_of_tests):
        funcs = input()
        num_of_elements = int(input())
        elements_input = input()[1:-1]
        if elements_input:
            elements = list(map(int, elements_input.split(",")))
        else:
            elements = []

        print(process_elements(funcs, elements, False))


if __name__ == "__main__":
    main()
