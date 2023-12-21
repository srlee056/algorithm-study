import sys


def is_blue(list):
    # return true if this LxL list is blue else False
    # check sum of all cell == L ** 2
    L = len(list)
    sum_of_all_cell = sum(sum(x) for x in list)
    # print(sum_of_all_cell)

    if sum_of_all_cell == L**2:
        return True
    else:
        return False


def is_white(list):
    L = len(list)
    # print(list)
    sum_of_all_cell = sum(sum(x) for x in list)
    # print(sum_of_all_cell)

    if sum_of_all_cell == 0:
        return True
    else:
        return False


def split_table(table):
    l = len(table) // 2
    t = [[[0 for _ in range(l)] for _ in range(l)] for _ in range(4)]

    for i in range(l):
        for j in range(l):
            t[0][i][j] = table[i][j]
            t[1][i][j] = table[i + l][j]
            t[2][i][j] = table[i][j + l]
            t[3][i][j] = table[i + l][j + l]

    """print(t[0])
    print(t[1])
    print(t[2])
    print(t[3])"""
    return t


# n is one of  2, 4, 8, 16, 32, 64, 128
n = int(sys.stdin.readline())

table = []
for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    table.append(row)

# print(table)
tables = [table[:]]

count_of_white, count_of_blue = 0, 0
while tables:
    table = tables.pop()
    x, y = len(table), len(table[0])
    # print(x, y, tables)
    if is_blue(table):
        count_of_blue += 1
    elif is_white(table):
        count_of_white += 1
    else:  # l == 1 인 경우는 위에서 걸러지므로, l >= 2 인 경우만 남게 된다
        tables = tables + split_table(table)

print(count_of_white)
print(count_of_blue)
