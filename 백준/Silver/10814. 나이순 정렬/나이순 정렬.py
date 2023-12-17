import sys

n = int(sys.stdin.readline())

users = {}
for _ in range(n):
    age, name = sys.stdin.readline().split()
    age = int(age)

    users[age] = users.get(age, [])
    users[age].append(name)

for age in sorted(users):
    for name in users[age]:
        print(f"{age} {name}")
