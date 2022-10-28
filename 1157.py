inputWord = input().upper()

countCharInWord = {}
maxCount = 0
maxCountChar = ''

for c in inputWord:
    countCharInWord.setdefault(c, 0)
    countCharInWord[c] += 1
    maxCount = max(maxCount, countCharInWord[c])

for k, v in countCharInWord.items():
    if v == maxCount : 
        if maxCountChar != '':
            maxCountChar = '?'
            break
        else:
            maxCountChar = k

print(maxCountChar)