def solution(numbers):
    answer = 0

    weight = [{} for _ in range(10)]

    initWeight(weight)

    # print(weight)

    shortest(weight)
    # print(weight)
    for k, v in weight[1].items():
        print(1, k, v)

    return answer


def initWeight(weight):
    zeroSDist = [3, 2, 3]
    for i, n in enumerate(zeroSDist):
        weight[0][i+7] = n
        weight[i+7][0] = n

    for i in range(10):
        weight[i][i] = 1
        if i == 0:
            continue
        if i % 3 != 0:
            if i <= 6:
                weight[i][i+4] = 3
            if i > 3:
                weight[i][i-2] = 3
            weight[i][i+1] = 2
        if i % 3 != 1:
            if i <= 6:
                weight[i][i+2] = 3
            if i > 3:
                weight[i][i-4] = 3
            weight[i][i-1] = 2
        if i <= 6:
            weight[i][i+3] = 2
        if i > 3:
            weight[i][i-3] = 2


def shortest(weight):

    route = deque([5])
    visited = [False for _ in range(10)]
    visited
    while route:
        curNode = route.popleft()
        visited[curNode] = True
        route.extend(list(curNode.keys()))

        print(route)
    for i in route:
        visited = [False for _ in range(10)]
        for k in weight[i].keys():
            visited[k] = True

        tempItems = list(weight[i].items())
        for k, v in tempItems:
            if k != i:
                for j in weight[k].keys():
                    newWeight = v + weight[k][j]
                    if not visited[j]:
                        weight[i][j] = newWeight
                        visited[j] = True
                    else:
                        weight[i][j] = min(newWeight, weight[i][j])
                    # if j == 0:
                        # print(i, k, newWeight)
        for k, v in weight[i].items():
            if i not in weight[k].keys():
                weight[k][i] = v
            else:
                weight[k][i] = min(v, weight[k][i])
