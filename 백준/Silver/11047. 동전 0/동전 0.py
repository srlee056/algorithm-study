from sys import stdin

n, k = map(int, stdin.readline().split())

coins = []
pointer = 0
for i in range(n):
    coin = int(stdin.readline().strip())
    coins.append(coin)
    if coin <= k:
        pointer = i

# print(k, coins, pointer)

counts = 0
while k > 0:
    counts += k // coins[pointer]
    k = k % coins[pointer]
    pointer -= 1

print(counts)
