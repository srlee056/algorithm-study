n = int(input())

threes = [0, 3, 6, 9, 12]

bagNum = -1

for t in threes:
    if n >= t and (n-t) %5 == 0 :
        bagNum = (n-t)//5 + t//3
        break
print(bagNum)
