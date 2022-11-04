n = int(input())

# n is between 3k(k-1)+1 < n <= 3k(k+1) + 1
# and k+1 is the answer
if n == 1 : print(1)
else :
    k = ((n-1)//3)**(1/2) 
    k = round(k)
    #print(k, n)
    if 3 * k * (k-1) < n-1 and 3 * k * (k+1) >= n-1:
        #print("hi")
        print(k+1)
    else :
        print(k+2)