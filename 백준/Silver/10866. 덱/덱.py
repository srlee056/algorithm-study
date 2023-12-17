import sys
from collections import deque


def push_front(x):
    deck.appendleft(x)


def push_back(x):
    deck.append(x)


def pop_front():
    print(deck.popleft() if deck else -1)


def pop_back():
    print(deck.pop() if deck else -1)


def size():
    print(len(deck))


def empty():
    print(0 if deck else 1)


def front():
    print(deck[0] if deck else -1)


def back():
    print(deck[-1] if deck else -1)


n = int(sys.stdin.readline())
deck = deque()

command_dict = {
    "push_front": push_front,
    "push_back": push_back,
    "pop_front": pop_front,
    "pop_back": pop_back,
    "size": size,
    "empty": empty,
    "front": front,
    "back": back,
}

for _ in range(n):
    commands = sys.stdin.readline().split()

    if commands[0] in ["push_front", "push_back"]:
        command_dict[commands[0]](commands[1])
    else:
        command_dict[commands[0]]()
