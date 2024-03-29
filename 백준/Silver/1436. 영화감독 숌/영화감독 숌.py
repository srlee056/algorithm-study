import sys

n = int(sys.stdin.readline())


sixes = set()


for i in range(10000):
    
    count = 4- len(str(i)) if i != 0 else 4
    
    #print(i, count)

    sixes.add(int(str(i)+"666"))
    for j in range(10 ** count):

        new_str = str(i)+"666"
        for k in range(0, count-len(str(j))+1):
            sixes.add(int(new_str + "0"*k+str(j)))


sorted_ = sorted(sixes)
#print(sorted_)
#print(len(sorted_))
print(sorted_[n-1])