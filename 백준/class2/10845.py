from collections import deque
import sys


def push(x):
    queue.append(x)


def size():
    print(len(queue))


def empty():
    print(0 if queue else 1)


def pop():
    print(queue.popleft() if queue else -1)


def front():
    print(queue[0] if queue else -1)


def back():
    print(queue[-1] if queue else -1)


n = int(sys.stdin.readline().rstrip())
queue = deque()
command_dict = {
    "push": push,
    "size": size,
    "empty": empty,
    "pop": pop,
    "front": front,
    "back": back,
}

for _ in range(n):
    commands = sys.stdin.readline().rstrip().split()
    if commands[0] == "push":
        command_dict[commands[0]](commands[1])
    else:
        command_dict[commands[0]]()
