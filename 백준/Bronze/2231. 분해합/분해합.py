from sys import stdin

n = stdin.readline().strip()

leng = len(n)

n = int(n)

muls = []
for i in range(leng):
    muls.append(10**i + 1)

result = []

while muls:
    mul = muls.pop()

    div = n // mul

    # 18 - 11 =7, (18 + 99 - 101 = 16), (18+99+909-1001=25) ...
    if mul == 11:
        if div == 0 and n % 2 != 0:
            break
        elif (n - div * mul) % 2 != 0:
            div -= 1
    elif n % mul <= (len(str(mul)) - 1) * 9 - 2:
        div -= 1

    if div > 9:
        div = 9
    n -= div * mul

    result.append(str(div))

if n != 0:
    print(0)
else:
    #print(result)
    print(int("".join(result)))
