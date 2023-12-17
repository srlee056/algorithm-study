import sys

n = int(sys.stdin.readline())

stack = []
for _ in range(n):
    commands = sys.stdin.readline().rstrip().split()

    if commands[0] == "push":
        stack.append(commands[1])
    elif commands[0] == "pop":
        if len(stack):
            print(stack.pop())
        else:
            print(-1)
    elif commands[0] == "size":
        print(len(stack))
    elif commands[0] == "empty":
        if len(stack):
            print(0)
        else:
            print(1)
    elif commands[0] == "top":
        if len(stack):
            print(stack[-1])
        else:
            print(-1)
