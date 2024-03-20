import sys

input = sys.stdin.readline

n, m = map(int, input().split())

not_seen = set()
not_heard = set()

for _ in range(n):
    not_seen.add(input().strip())

for _ in range(m):
    not_heard.add(input().strip())

not_seen_heard = not_seen & not_heard
print(len(not_seen_heard))
for people in sorted(not_seen_heard):
    print(people)
