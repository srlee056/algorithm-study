import sys

n = int(sys.stdin.readline())
words = [sys.stdin.readline().rstrip() for i in range(n)]

words = list(set(words))
words.sort(key=lambda x: (len(x), x))

for word in words:
    print(word)
