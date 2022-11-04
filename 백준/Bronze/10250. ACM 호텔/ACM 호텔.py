import sys

t = int(input())
rooms = []

for _ in range(t):
    h, w, n = map(int, sys.stdin.readline().strip().split())

    roomNum = str((n-1)//h + 1)
    roomNum = str((n-1)%h + 1) + roomNum.zfill(2)
    
    rooms.append(roomNum)

for r in rooms:
    print(r)