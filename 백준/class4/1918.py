import sys
import re

input_str = sys.stdin.readline().strip()


# find () and make them postprefix
# find *, / and make them postprefix
# find +, - and make them postprefixA

operator_stack = []
operand_str = ""
operators = ["+", "-", "*", "/", "(", ")"]
for i, s in enumerate(input_str):
    if s in operators:
        if operator_stack:
            op = operator_stack.pop()
        operator_stack.append(s)
    else:
        operand_str += "s"

https://wikidocs.net/192123