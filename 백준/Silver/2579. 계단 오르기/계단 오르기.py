from sys import stdin
from collections import deque

n = int(stdin.readline())

scores = [0]
for _ in range(n):
    scores.append(int(stdin.readline()))

score_streaks = [[0, 0] for _ in range(n + 1)]
score_streaks[1] = [scores[1], 0]

for i in range(2, n + 1):
    score_streaks[i][0] = max(score_streaks[i - 2]) + scores[i]
    score_streaks[i][1] = score_streaks[i - 1][0] + scores[i]

print(max(score_streaks[n]))
