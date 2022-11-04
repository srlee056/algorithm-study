t = int(input())
results = []
for _ in range(t):
    k = int(input())
    n = int(input())

    rooms = [[] for _ in range(k+1)]
    rooms[0] = [num+1 for num in range(n)]

    for i in range(1, k+1):
        for j in range(n):
            rooms[i].append(sum(rooms[i-1][:j+1]))
    
    results.append(rooms[k][n-1])

print(*results, sep = "\n")
