import sys


def add(x):
    if x not in _set:
        _set.add(x)


def remove(x):
    if x in _set:
        _set.remove(x)


def check(x):
    if x in _set:
        print(1)
    else:
        print(0)


def toggle(x):
    if x in _set:
        remove(x)
    else:
        add(x)


def _all():
    return set([i for i in range(1, 21)])


def empty():
    return set()


_set = set()

m = int(sys.stdin.readline())

commands = {
    "add": add,
    "remove": remove,
    "check": check,
    "toggle": toggle,
    "all": _all,
    "empty": empty,
}

for _ in range(m):
    command = sys.stdin.readline().split()
    if command[0] in ["all", "empty"]:
        _set = commands[command[0]]()
        # print(_set)
    else:
        commands[command[0]](int(command[1]))
