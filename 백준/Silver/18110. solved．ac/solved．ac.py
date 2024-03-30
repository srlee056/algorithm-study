from sys import stdin

n = int(stdin.readline())

difficulties = [0 for _ in range(31)]
for _ in range(n):
    difficulties[int(stdin.readline())] += 1

# print(difficulties)


rm_num = int(sum(difficulties) * 0.15 + 0.5)


# print(rm_num)

if n == 0:
    print(n)
else:
    left_count, right_count = rm_num, rm_num
    for i in range(1, 31):
        if left_count == 0 and right_count == 0:
            break
        if difficulties[i] != 0:
            if 0 < left_count <= difficulties[i]:
                difficulties[i] -= left_count
                left_count = 0
            elif left_count > difficulties[i]:
                left_count -= difficulties[i]
                difficulties[i] = 0
        if difficulties[-i] != 0:
            if 0 < right_count <= difficulties[-i]:
                difficulties[-i] -= right_count
                right_count = 0
            elif right_count > difficulties[-i]:
                right_count -= difficulties[-i]
                difficulties[-i] = 0

    # print(difficulties)
    print(
        int(sum([i * n for i, n in enumerate(difficulties)]) / sum(difficulties) + 0.5)
    )
