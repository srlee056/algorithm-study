import sys
from collections import defaultdict, deque

def main():
    n = int(sys.stdin.readline().strip())

    arr = []
    for _ in range(n):
        row = list(map(int, sys.stdin.readline().split()))
        arr.append(row)
    
    combinations = []
    backtrack(n, [], combinations)

    m = len(combinations)//2

    min_diff = 10000
    for idx in range(m):
        start, link = combinations[idx], combinations[2*m-1-idx]
        diff = get_stat_diff(arr, start, link)
        min_diff = min(min_diff, diff)

    print(min_diff)
    

def backtrack(n, start, combinations):
    if len(start) == n//2:
        return combinations.append(start)

    startidx = 0 if len(start) == 0 else start[-1]+1
    for i in range(startidx, n):
        backtrack(n, start+[i], combinations)


def get_stat_diff(arr, start, link):
    sum_start, sum_link = 0, 0
    for i in start:
        for j in start:
            if i != j:
                sum_start += arr[i][j]
    for i in link:
        for j in link:
            if i != j:
                sum_link += arr[i][j]
    return abs(sum_start-sum_link)



if __name__=="__main__":
    main()

