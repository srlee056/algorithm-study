originNumber = int(input())

a, b = originNumber//10, originNumber%10
lenghtOfCycle = 1

while True:
    newB = (a+b)%10
    a = b
    b = newB
    if a*10+b == originNumber:
        break
    else : 
        lenghtOfCycle += 1
    
print(lenghtOfCycle)