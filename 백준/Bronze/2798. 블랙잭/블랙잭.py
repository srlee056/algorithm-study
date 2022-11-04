n, m = map(int, input().strip().split())

cards = list(map(int, input().strip().split()))

# pick only 3 cards 

#print(cards)
maxSum = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            cardSum = cards[i]+ cards[j]+ cards[k]
            if cardSum <= m and maxSum < cardSum :
                maxSum = cardSum

print(maxSum)

