import sys

n = int(sys.stdin.readline())

spending_time = list(map(int, sys.stdin.readline().split()))

# 그리디 알고리즘 적용
# 대기 시간의 총 누적 합을 최소로 하려면, 인출하는데 가장 짧은 시간이 걸리는 사람을 제일 앞에, 오랜 시간이 걸리는 사람을 제일 뒤에 두어야 한다.
spending_time.sort()

total_sum = 0
for idx, time in enumerate(spending_time):
    total_sum += (n - idx) * time

print(total_sum)
