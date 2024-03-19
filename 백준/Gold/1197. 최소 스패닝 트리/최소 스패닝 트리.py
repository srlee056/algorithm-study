import sys

# Using Kruskal Algorithm
sys.setrecursionlimit(10**9)


def find(parent_node, v):
    # 경로 압축
    if parent_node[v] != v:
        parent_node[v] = find(parent_node, parent_node[v])
    return parent_node[v]


def main():
    input = sys.stdin.readline

    v, e = map(int, input().split())

    edges = []
    for _ in range(e):
        edges.append(list(map(int, input().split())))

    # sort edge by weight
    edges = sorted(edges, key=lambda x: x[2], reverse=True)

    parent_node = [i for i in range(v + 1)]

    total_weight = 0
    while edges:
        v1, v2, w = edges.pop()
        r1 = find(parent_node, v1)
        r2 = find(parent_node, v2)
        if r1 == r2:  # when two node are in the same set
            continue

        parent_node[r2] = r1  # union
        total_weight += w
    print(total_weight)


if __name__ == "__main__":
    main()
