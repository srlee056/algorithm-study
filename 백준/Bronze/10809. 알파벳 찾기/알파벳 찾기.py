import sys

word = sys.stdin.readline().strip()

alphabet = [-1 for _ in range(26)]


for i, char in enumerate(word):
    check = alphabet[ord(char) - 97]
    alphabet[ord(char) - 97] = i if check == -1 else check

print(' '.join(map(str, alphabet)))