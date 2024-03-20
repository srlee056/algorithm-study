import sys
from collections import deque


def remove(heap):
    if not heap:
        return 0
    # print(heap)
    result_value = heap.popleft()
    # print(result_value)
    if heap:
        heap.appendleft(heap.pop())
    cur_idx = 0
    len_heap = len(heap)
    while cur_idx < len_heap:
        # print("cur_idx", cur_idx)
        left_idx = cur_idx * 2 + 1
        right_idx = cur_idx * 2 + 2

        if left_idx >= len_heap:
            break
        elif left_idx < len_heap <= right_idx:
            target_idx = left_idx
        elif heap[left_idx] <= heap[right_idx]:
            target_idx = left_idx
        else:
            target_idx = right_idx

        if heap[target_idx] < heap[cur_idx]:
            heap[cur_idx], heap[target_idx] = heap[target_idx], heap[cur_idx]
            # print("after reordering", heap)
            cur_idx = target_idx
        else:
            break

    return result_value


def add(heap, x):
    heap.append(x)
    cur_idx = len(heap) - 1

    while cur_idx > 0:
        parent_idx = (cur_idx - 1) // 2

        if heap[parent_idx] <= heap[cur_idx]:
            break

        heap[cur_idx], heap[parent_idx] = heap[parent_idx], heap[cur_idx]
        cur_idx = parent_idx

    # print(heap)


def main():
    input = sys.stdin.readline

    n = int(input())
    heap = deque([])
    input_list = []
    for _ in range(n):
        input_list.append(int(input()))

    for i in input_list:
        if i == 0:
            print(remove(heap))
        else:
            add(heap, i)


if __name__ == "__main__":
    main()
