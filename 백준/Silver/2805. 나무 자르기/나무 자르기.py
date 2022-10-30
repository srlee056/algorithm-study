n, m = map(int, input().split())

trees = list(map(int, input().split()))

#print(n, m)
#print(trees)
minH = 0
maxH = max(trees)

while minH < maxH-1 :
    setH = (minH+maxH+1) // 2
    #print( minH, maxH, setH)
    cutTrees = [0 if setH > t else t-setH
                         for t in trees]
    #print(cutTrees)
    #print(sum(cutTrees))
    if sum(cutTrees) >= m : minH = setH 
    else : maxH= setH

print(minH)