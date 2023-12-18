import sys

# input()보다 훨씬 빠르다
# sys.stdin.readline()은 개행문자까지 입력받기 때문에
# rstrip()을 통해 개행문자를 제거해준다

n = int(sys.stdin.readline())
words = [sys.stdin.readline().rstrip() for i in range(n)]

words = list(set(words))
words.sort(key=lambda x: (len(x), x))

for word in words:
    print(word)
