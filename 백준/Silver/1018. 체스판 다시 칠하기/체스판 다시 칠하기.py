import sys

h, w = map(int, input().split())

board = [sys.stdin.readline().strip() for _ in range(h)]
#print(h, w)
#print(board)
compareBoard = []
for hi in range(h):
    line = []
    for wi in range(w):
        if board[hi][wi] == 'W': line.append((hi+wi)%2)
        elif board[hi][wi] == 'B': line.append((hi+wi+1)%2)

    #print(hi)
    #print(line)
    #print(board[hi])
    compareBoard.append(line)

#print(compareBoard)

minSum = 32

for hi in range(h-7):
    for wi in range(w-7):
        sumTemp= 0
        #print(hi, wi)
        #print(compareBoard[hi][wi:wi+8])
        for i in range(8):
            sumTemp += sum(compareBoard[hi+i][wi:wi+8])
        
        minSum = min(minSum, sumTemp, (64-sumTemp))

print(minSum)