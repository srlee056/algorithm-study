import sys

num_of_computers = int(sys.stdin.readline())
num_of_networks = int(sys.stdin.readline())

networks = []

for _ in range(num_of_networks):
    v1, v2 = map(int, sys.stdin.readline().split())
    networks.append([v1, v2])
    networks.append([v2, v1])

# print(networks)

is_visited = {i + 1: False for i in range(num_of_computers)}

computers = [1]

while computers:
    computer = computers.pop()
    is_visited[computer] = True
    for network in networks:
        # 네트워크를 확인해서 이 컴퓨터와 연결된 다른 컴퓨터를 확인
        # 연결된 컴퓨터가 방문한 적이 없는 경우, computers에 추가하여 이후에 네트워크를 확인
        if network[0] == computer and not is_visited[network[1]]:
            computers.append(network[1])

# print(is_visited)

num_of_infected_computers = sum(1 for v in is_visited.values() if v) - 1

print(num_of_infected_computers)
