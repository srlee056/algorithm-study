import sys

n = int(sys.stdin.readline())

colors = ["red", "green", "blue"]

cost_of_colors = []
for _ in range(n):
    red, green, blue = map(int, sys.stdin.readline().split())
    cost = {"red": red, "green": green, "blue": blue}
    cost_of_colors.append(cost)

paints = [{"red": 0, "green": 0, "blue": 0}]

for i in range(1, n + 1):
    red = (
        min(paints[i - 1]["green"], paints[i - 1]["blue"])
        + cost_of_colors[i - 1]["red"]
    )
    green = (
        min(paints[i - 1]["red"], paints[i - 1]["blue"])
        + cost_of_colors[i - 1]["green"]
    )
    blue = (
        min(paints[i - 1]["green"], paints[i - 1]["red"])
        + cost_of_colors[i - 1]["blue"]
    )
    paints.append({"red": red, "green": green, "blue": blue})

print(min(paints[-1].values()))
