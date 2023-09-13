n, l = map(int, input().split())

while l <= 100:
    a, b = -1, -1
    if (2 * n) % l == 0 :
        #b-a = l-1
        #a+b = (2 * n) // l 

        if ((2 * n)//l + l - 1) % 2 == 0 :            
            b = ((2 * n)//l + l - 1) // 2
            a = ((2 * n)//l - l + 1) // 2 
            if a >=0 and b >= 0:
                break
    l += 1

if a == -1 : print(-1)
else : 
    result = ' '.join([str(i) for i in range(a, b+1)])
    print(result)    