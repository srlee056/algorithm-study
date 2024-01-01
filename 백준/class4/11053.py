import sys

n = int(sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().split()))

sequences = [[0] for _ in range(n)]
sequences[0].append(numbers[0])

for i in range(1, n):
    # compare with sequences[i-1]
    for j in range(len(sequences[i - 1])):
        if sequences[i - 1][j] < numbers[i]:
            if j + 1 < len(sequences[i - 1]):
                sequences[i].append(min(numbers[i], sequences[i - 1][j + 1]))
            else:
                sequences[i].append(numbers[i])
        else:
            if j + 1 < len(sequences[i - 1]):
                sequences[i].append(sequences[i - 1][j + 1])


print(len(sequences[-1]) - 1)
