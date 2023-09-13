num = int(input())

# num * num 2차 리스트 or 저장소 선언
friendList = ['' for _ in range(num)]

for i in range(num):
   friendList[i] = input()

#numberOfFriends = [0 for _ in range(num)]
#numberOfFriends = [friendList[j].count('Y') for j in range(num)]
#sndFr = [0 for _ in range(num)]
frDist = [[0 for _ in range(num)] for _ in range(num)]
fstFrSet = [set() for _ in range(num)]

for j in range(num):
   fstFrSet[j] = set([k for k in range(num) if (friendList[j][k]=='Y')])  

sndFrSet = fstFrSet.copy()
#print(fstFrSet)

for j in range(num):
   for x in fstFrSet[j]:
      sndFrSet[j] = sndFrSet[j].union(fstFrSet[x])
      sndFrSet[j].remove(j)


print(max([len(sndFrSet[x]) for x in range(num)]))