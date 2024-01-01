import sys


str1 = sys.stdin.readline().rstrip()
str2 = sys.stdin.readline().rstrip()

str1_dict = {}
for i, c in enumerate(str1):
    str1_dict[c] = str1_dict.get(c, [])
    str1_dict[c].append(i)

sequences = [list(str2)]

str2_list = sequences[0]
for i in range(1, len(str2_list)):
    prev, cur = str2_list[i - 1], str2_list[i]
    if str1_dict[prev][0] < str1_dict[cur][0]:
        str2_list[i] = str2_list[i - 1]

next_row = []

for i in range(len(str2_list) - 1):
    next_row.append(str2_list[i] + str2[i + 1])

print(next_row)
print(str2_list)
