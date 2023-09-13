num = int(input())

friendList = ['' for _ in range(num)]

for i in range(num):
   friendList[i] = input()

frDist = [[0 for _ in range(num)] for _ in range(num)]
fstFrSet = [set() for _ in range(num)]

for j in range(num):
   fstFrSet[j] = set([k for k in range(num) if (friendList[j][k]=='Y')])  

sndFrSet = fstFrSet.copy()

for j in range(num):
   for x in fstFrSet[j]:
      sndFrSet[j] = sndFrSet[j].union(fstFrSet[x])
      sndFrSet[j].remove(j)


print(max([len(sndFrSet[x]) for x in range(num)]))