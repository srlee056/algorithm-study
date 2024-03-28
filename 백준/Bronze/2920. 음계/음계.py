import sys

list = list(map(int, sys.stdin.readline().split()))
ceil = len(list)


ascending = True if list[0] == 1 else False
descending = True if list[-1] == 1 else False


for i in range(ceil):
    if ascending and list[i] == i+1:
        pass
    elif descending and list[i] == ceil - i:
        pass
    else:
        ascending, descending = False, False
        break

if ascending and not descending:
    print("ascending")
elif descending and not ascending:
    print("descending")
else:
    print("mixed")

