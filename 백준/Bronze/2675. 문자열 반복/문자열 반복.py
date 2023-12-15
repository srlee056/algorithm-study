n = int(input())


for i in range(n):
    repeat, str = input().split()
    repeat = int(repeat)

    result = ""
    for s in str:
        result += s * repeat
    print(result)
