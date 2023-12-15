n = int(input())
nums = map(int, input().split())

min_num, max_num = 1000000, -1000000
for num in nums:
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num

print(min_num, max_num)
