import sys

num_of_computers = int(sys.stdin.readline())
num_of_networks = int(sys.stdin.readline())

# 각 컴퓨터마다 연결된 컴퓨터를 저장할 set() 변수를 생성
# 입력으로 받는 컴퓨터 번호는 0이 아니라 1부터 시작하므로, range를 다음과 같이 설정
networks = [set() for _ in range(num_of_computers + 1)]

for _ in range(num_of_networks):
    v1, v2 = map(int, sys.stdin.readline().split())
    networks[v1].add(v2)
    networks[v2].add(v1)

# 방문한 컴퓨터를 저장할 변수와, 방문 할 컴퓨터를 저장할 변수를 각각 생성
visited_computers = set()

computers_to_visit = [1]

while computers_to_visit:
    cur_computer = computers_to_visit.pop()

    if cur_computer not in visited_computers:
        visited_computers.add(cur_computer)
        # 방문할 컴퓨터는 cur_computer와 연결되어있으면서, 방문한 적 없는 컴퓨터여야 함
        # set operation `-` 사용하여 위 조건의 컴퓨터를 계산
        computers_to_visit.extend(networks[cur_computer] - visited_computers)

num_of_infected_computers = len(visited_computers) - 1

print(num_of_infected_computers)
