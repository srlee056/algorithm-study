import sys


pal_pair = {')': '(', ']':'['}
result = []
while True:
    palindrom = []
    input_line = sys.stdin.readline().rstrip()
    if input_line == '.':
        break
    else:
        word = "yes"
        for char in input_line:
            if char in ['(', '[']:
                palindrom.append(char)
            elif char in [')', ']']:
                if not palindrom or pal_pair[char] != palindrom.pop():
                    word = "no"
                    break
        if len(palindrom) > 0:
            word = "no"
        result.append(word)

for str in result:
    print(str)
    