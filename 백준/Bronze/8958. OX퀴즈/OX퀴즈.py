import sys

input = sys.stdin.readline

n = int(input().strip())

scores = []
for _ in range(n):
    ox_str = input().strip()
    score = 0
    count = 0
    for char in ox_str:
        if char == 'O':
            count += 1
            score += count
        elif char == 'X' :
            count = 0
    
    scores.append(score)

for score in scores:
    print(score)