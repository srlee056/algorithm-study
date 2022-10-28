n = int(input())
# find how many 5배수s smaller then n
fives = 0
while True:
    n = n // 5
    fives += n

    if n < 5 : break

print(fives)    
