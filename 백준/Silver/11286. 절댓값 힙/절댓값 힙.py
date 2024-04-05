import sys
from collections import deque


def heappush(heap, num):
    idx = len(heap)
    heap.append(num)

    while idx > 0:
        parent = (idx - 1) // 2

        if abs(heap[idx]) < abs(heap[parent]) or (
            abs(heap[idx]) == abs(heap[parent]) and heap[idx] < heap[parent]
        ):
            heap[idx], heap[parent] = heap[parent], heap[idx]
            idx = parent
        else:
            break


def heappop(heap):
    if heap:
        result = heap.popleft()
    else:
        return 0

    if heap:
        heap.appendleft(heap.pop())

    idx = 0
    while idx < len(heap):
        left, right = 2 * idx + 1, 2 * idx + 2
        if left >= len(heap):
            break
        elif right >= len(heap):
            small = left
        elif (
            abs(heap[left]) < abs(heap[right])
            or abs(heap[left]) == abs(heap[right])
            and heap[left] < heap[right]
        ):
            small = left
        else:
            small = right

        if abs(heap[small]) < abs(heap[idx]) or (
            abs(heap[small]) == abs(heap[idx]) and heap[small] < heap[idx]
        ):
            heap[small], heap[idx] = heap[idx], heap[small]
            idx = small
        else:
            break

    return result


def main():

    n = int(sys.stdin.readline().strip())

    inputs = []
    abs_heap = deque([])
    for _ in range(n):
        inputs.append(int(sys.stdin.readline().strip()))

    for m in inputs:
        if m == 0:
            print(heappop(abs_heap))
        else:
            heappush(abs_heap, m)


if __name__ == "__main__":
    main()
