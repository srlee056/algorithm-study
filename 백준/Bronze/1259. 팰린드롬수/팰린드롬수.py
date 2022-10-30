wordList = []
while True:
    inputWord = input().strip()
    if inputWord == '0': break
    else : wordList.append(inputWord)
    
for w in wordList:
    result = 'yes'
    for i in range(len(w)//2):
        if w[i] != w[len(w)-1-i] : result = 'no'

    print(result)