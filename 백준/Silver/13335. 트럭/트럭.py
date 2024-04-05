import sys
from collections import deque

n, length, weight = map(int, sys.stdin.readline().split())

trucks = deque(map(int, sys.stdin.readline().split()))

bridge = deque([])
truck_w_sum = 0
time = 0
while trucks:
    if len(bridge) == length:
        w = bridge.popleft()
        if w != -1:
            truck_w_sum -= w

    truck = trucks.popleft()
    if truck_w_sum + truck <= weight:
        bridge.append(truck)
        truck_w_sum += truck
    else:
        trucks.appendleft(truck)
        bridge.append(-1)
    time += 1

time += length

print(time)
