l = int(input())

alphabetList = input().strip()

r, m = 31, 1234567891
hashSum = 0 

#print(alphabetList[0], ord(alphabetList[0]))
# ord('a') is 97 in this encoding system(?)
for i in range(l):
    hashSum += (ord(alphabetList[i])-96) * (r**i)

print(hashSum % m)
