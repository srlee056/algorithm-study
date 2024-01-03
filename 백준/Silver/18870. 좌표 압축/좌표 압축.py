import sys

n = int(sys.stdin.readline())

x_list = list(map(int, sys.stdin.readline().split()))

# 중복을 제외한 후 리스트를 정렬시킨다.
sorted_x_list = sorted(set(x_list))
sorted_x_dict = {}
for i, x in enumerate(sorted_x_list):
    if x not in sorted_x_dict:
        sorted_x_dict[x] = i

zipped_x_list = [sorted_x_dict[x] for x in x_list]


print(" ".join(map(str, zipped_x_list)))
