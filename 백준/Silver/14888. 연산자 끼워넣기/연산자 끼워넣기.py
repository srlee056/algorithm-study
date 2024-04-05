import sys
from collections import deque

n = int(sys.stdin.readline().strip())
operands = list(map(int, sys.stdin.readline().split()))
operators = list(map(int, sys.stdin.readline().split()))  # +, -, *, /


def dfs(operands, i, operators):
    num = operands[i]
    if i == 0:
        return [num]
    plus, minus, multiply, devide = operators

    results = []
    # print(i, operands, operators)
    if plus > 0:
        pl_num = dfs(operands, i - 1, [plus - 1, minus, multiply, devide])
        for pl in pl_num:
            results.append(pl + num)
        # print("plus", results)
    if minus > 0:
        mi_num = dfs(operands, i - 1, [plus, minus - 1, multiply, devide])
        for mi in mi_num:
            results.append(mi - num)
        # print("plus", results)
    if multiply > 0:
        ml_num = dfs(operands, i - 1, [plus, minus, multiply - 1, devide])
        for ml in ml_num:
            results.append(ml * num)
        # print("plus", results)
    if devide > 0:
        dv_num = dfs(operands, i - 1, [plus, minus, multiply, devide - 1])
        for dv in dv_num:
            result = abs(dv) // num * (-1) if dv < 0 else dv // num
            results.append(result)
        # print("plus", results)

    # print(i, results)
    return results


rr = dfs(operands, n - 1, operators)
# print(rr)
print(max(rr))
print(min(rr))
