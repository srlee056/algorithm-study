import sys


def splitAndMerge(bigList):
    l = len(bigList)
    #print(bigList)
    if l <= 1 : return bigList
    
    aList = splitAndMerge(bigList[:l//2])
    bList = splitAndMerge(bigList[l//2:])
    #print(aList, bList)

    newList = []
    ai, bi = 0, 0
    while ai < len(aList) and bi <len(bList):
        if aList[ai] < bList[bi]:
            newList.append(aList[ai])
            ai += 1
        else :
            newList.append(bList[bi])
            bi += 1

    for i in range(ai, len(aList)) :
        newList.append(aList[i])
    for j in range(bi, len(bList)):
        newList.append(bList[j])

    return newList




if __name__ == "__main__":
    n = int(input())

    orderList = []
    for _ in range(n):
        m = int(sys.stdin.readline())
        orderList.append(m)

    #print(orderList)
    #print('mergesort start')
    newList = (splitAndMerge(orderList))
    #print(newList)
    for n in newList:
        print(n)