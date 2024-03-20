import sys
import heapq
from collections import deque

# using Prim Algorithm

# 일단 모든 정점은 1~v로 입력이 주어진다고 가정,
# v1, v2 에서 v1==v2일 수 있음


def add_to_heap(heap, node, weight):
    cur_idx = len(heap)
    heap.append((node, weight))
    # print("add_to_heap", heap, node, weight)
    while cur_idx > 0:
        parent_idx = (cur_idx - 1) // 2
        if (
            heap[cur_idx][1] < heap[parent_idx][1]
        ):  # compare weight and change when current is smaller
            heap[cur_idx], heap[parent_idx] = heap[parent_idx], heap[cur_idx]
            cur_idx = parent_idx
        else:
            break


def remove_from_heap(heap):
    last_idx = len(heap) - 1
    return_value = heap[0]
    cur_idx = 0
    # print("remove_from_heap", heap)
    while cur_idx <= last_idx:
        # print(cur_idx, heap[cur_idx])
        left_idx = cur_idx * 2 + 1
        right_idx = cur_idx * 2 + 2
        if left_idx > last_idx:
            break
        elif right_idx > last_idx:
            target_idx = left_idx
        elif heap[left_idx][1] <= heap[right_idx][1]:  # compare weight
            target_idx = left_idx
        else:
            target_idx = right_idx

        heap[cur_idx] = heap[target_idx]

        cur_idx = target_idx

    # print(cur_idx, last_idx)
    if cur_idx in [last_idx - 1, last_idx - 2]:
        heap[cur_idx] = heap[last_idx]
    # if cur_idx do not have child -> last element would be set to cur_idx position
    # if cur_idx is left child
    heap.pop()
    # print("after ordering", heap)
    return return_value


def main():

    input = sys.stdin.readline

    v = int(input().strip())
    e = int(input().strip())

    adj_nodes = {}
    for _ in range(e):
        v1, v2, w = list(map(int, input().split()))
        adj_nodes[v1] = adj_nodes.get(v1, [])
        adj_nodes[v1].append((w, v2))
        adj_nodes[v2] = adj_nodes.get(v2, [])
        adj_nodes[v2].append((w, v1))

    # print(adj_nodes)

    start_node = 1
    # heapq use first element of tuple
    priority_queue = [(0, start_node)]
    visited = [False for _ in range(v + 1)]
    # visited[start_node] = True

    total_weight = 0
    while priority_queue:
        weight, node = heapq.heappop(priority_queue)
        # print(node, weight)
        if visited[node]:
            continue
        visited[node] = True

        # add adj_nodes[node] to priority_queue, min heap
        # that node2, weight2 -> if visited[node2] then do not add
        for w, n in adj_nodes[node]:
            # print(w, n)
            if not visited[n]:
                heapq.heappush(priority_queue, (w, n))
        # print("added:", node, weight)
        total_weight += weight
    print(total_weight)


if __name__ == "__main__":
    main()
