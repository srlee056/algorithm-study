import sys


def push(x):
    stack.append(x)


def pop():
    print(stack.pop() if stack else -1)


def size():
    print(len(stack))


def empty():
    print(0 if stack else 1)


def top():
    print(stack[-1] if stack else -1)


n = int(sys.stdin.readline())
stack = []
command_dict = {"push": push, "pop": pop, "size": size, "empty": empty, "top": top}

for _ in range(n):
    commands = sys.stdin.readline().rstrip().split()
    if commands[0] == "push":
        command_dict[commands[0]](int(commands[1]))
    else:
        command_dict[commands[0]]()
