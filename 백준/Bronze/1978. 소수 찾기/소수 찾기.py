import sys


def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False
    return True


def main():
    n = int(sys.stdin.readline())

    numbers = map(int, sys.stdin.readline().split())

    # 2. 입력받은 수 각각이 소수인지를 판단한다.

    count = 0
    for num in numbers:
        if is_prime(num):
            count += 1

    print(count)


if __name__ == "__main__":
    main()
