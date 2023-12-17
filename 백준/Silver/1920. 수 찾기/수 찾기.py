import sys

n = int(sys.stdin.readline())
numbers_list = sys.stdin.readline().split()

m = int(sys.stdin.readline())
candidates_list = sys.stdin.readline().split()

numbers_dict = {}
for number in numbers_list:
    if number not in numbers_dict:
        numbers_dict[number] = 1


for candidate in candidates_list:
    is_in = numbers_dict.get(candidate, 0)
    print(is_in)
