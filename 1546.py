numberOfSubject = int(input())
scores = list(map(int, input().split()))
maxScore = max(scores)

newAverage = (sum(scores)/numberOfSubject) * (100/maxScore)

print(newAverage)