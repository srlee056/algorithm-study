n = int(input())
m = int(input())
s = input()
pn = 'IO'*n + 'I'
pdx, counts = -1, 0
while True:
    pdx = s.find(pn, pdx+1)
    if pdx==-1: break
    counts += 1
print(counts)