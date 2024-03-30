from sys import stdin

N, M, B = map(int, stdin.readline().split())

heights = [0] * 257
total_sum = 0

min_v, max_v = 256, 0
for _ in range(N):
    row = list(map(int, stdin.readline().split()))
    for value in row:
        heights[value] += 1
        min_v = min(min_v, value)
        max_v = max(max_v, value)
# print(heights)
acm_counts = [0] * 257
acm_counts[0] = heights[0]
for i in range(1, 257):
    acm_counts[i] = acm_counts[i - 1] + heights[i]
for i in range(1, 257):
    acm_counts[i] += acm_counts[i - 1]
# print(acm_counts)

acm_counts_rev = [0] * 257
acm_counts_rev[256] = heights[256]
for i in range(255, -1, -1):
    acm_counts_rev[i] = acm_counts_rev[i + 1] + heights[i]
for i in range(255, -1, -1):
    acm_counts_rev[i] += acm_counts_rev[i + 1]

# print(acm_counts_rev)
min_time = -1
min_time_h = 0
for k in range(min_v, max_v + 1):
    total_time = 0
    total_block = 0
    if k > 0:
        total_time += acm_counts[k - 1]
        total_block += acm_counts[k - 1]
    if k < 256:
        total_time += acm_counts_rev[k + 1] * 2
        total_block -= acm_counts_rev[k + 1]

    # print(total_time, total_block)
    if total_block <= B:
        if min_time == -1 or min_time >= total_time:
            min_time = total_time
            min_time_h = k

print(min_time, min_time_h)
