import sys
from collections import defaultdict, deque
import math
import heapq


def main():
    v, e = map(int, sys.stdin.readline().split())
    start_node = int(sys.stdin.readline().strip()) - 1

    dist_arr = [{} for _ in range(v)]

    for _ in range(e):
        from_, to_, dist = map(int, sys.stdin.readline().split())
        if (to_ - 1) in dist_arr[from_ - 1]:
            dist_arr[from_ - 1][to_ - 1] = min(dist_arr[from_ - 1][to_ - 1], dist)
        else:
            dist_arr[from_ - 1][to_ - 1] = dist

    visited = [False for _ in range(v)]

    heap = []
    for n, d in dist_arr[start_node].items():
        heapq.heappush(heap, (d, n))

    while heap:
        # find not visited, min_dist node
        if heap:
            min_dist, min_node = heapq.heappop(heap)
        else:
            break
        if visited[min_node]:
            continue
        # print("cur, min node", start_node, min_node)

        visited[min_node] = True
        for node_, dist_ in dist_arr[min_node].items():
            if (
                node_ in dist_arr[start_node]
                and dist_arr[start_node][node_] < dist_ + min_dist
            ):
                pass
            else:
                dist_arr[start_node][node_] = dist_ + min_dist
                heapq.heappush(heap, (dist_arr[start_node][node_], node_))

    for i in range(v):
        if i == start_node:
            print(0)
        elif i in dist_arr[start_node]:
            print(dist_arr[start_node][i])
        else:
            print("INF")


if __name__ == "__main__":
    main()
