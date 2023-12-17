import sys

n = int(sys.stdin.readline())

numbers = []


numbers = map(int, sys.stdin.readline().split())

# print(numbers)

# 1. 1000 이하의 소수 리스트를 생성해두고, 이 안에 존재하는지 확인한다.
# 2. 1000 이하의 소수라면, 31 이하의 소수로 나누어져야 한다.

prime_numbers = {1: False}

for i in range(2, 1001):
    if i not in prime_numbers:
        prime_numbers[i] = True
        for m in range(2, 1000 // i + 1):
            prime_numbers[i * m] = False

count = 0
for num in numbers:
    if prime_numbers[num]:
        count += 1

print(count)
