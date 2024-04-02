from sys import stdin
from collections import deque


def heap_push(heap, m):
    i = len(heap)
    heap.append(m)
    while i > 0:
        parent_i = (i - 1) // 2
        if heap[parent_i] < heap[i]:
            heap[parent_i], heap[i] = heap[i], heap[parent_i]
        else:
            break
        i = parent_i
    # print(heap)


def heap_pop(heap):
    if not heap:
        return 0

    result = heap.popleft()
    if heap:
        heap.appendleft(heap.pop())
        i = 0
        while i < len(heap):
            child_i1, child_i2 = 2 * (i + 1) - 1, 2 * (i + 1)
            if len(heap) <= child_i1:
                break
            elif child_i2 < len(heap) and heap[child_i1] < heap[child_i2]:
                child_i1, child_i2 = child_i2, child_i1

            if heap[i] >= heap[child_i1]:
                break
            else:
                heap[child_i1], heap[i] = heap[i], heap[child_i1]
            i = child_i1

    # print(heap)
    return result


def main():
    n = int(stdin.readline())

    heap = deque([])
    for _ in range(n):
        m = int(stdin.readline())
        if m == 0:
            print(heap_pop(heap))
        else:
            heap_push(heap, m)


if __name__ == "__main__":
    main()
