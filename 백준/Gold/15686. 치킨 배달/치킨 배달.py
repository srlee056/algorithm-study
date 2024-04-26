import sys
from collections import defaultdict, deque
from itertools import combinations

def main():
    n, m = map(int,sys.stdin.readline().split())

    arr = []
    home_points = []
    chicken_points = []
    for i in range(n):
        row = list(map(int, sys.stdin.readline().split()))
        for j, ele in enumerate(row):
            if ele == 1:
                home_points.append((i, j))
            elif ele == 2:
                chicken_points.append((i, j))
        arr.append(row)
    
    # get m of chicken_points

    all_survived_chicken_points = list(combinations(chicken_points, m))

    min_sum_dist = 10000
    for scp in all_survived_chicken_points:
        min_sum_dist = min(min_sum_dist, get_distance_sum(home_points, scp))

    print(min_sum_dist)

def get_distance_sum(home_points, chicken_points):

    
    sum_dist = 0
    for hx, hy in home_points:
        min_dist = 1000
        for cx, cy in chicken_points:
            min_dist = min(min_dist, abs(hx-cx)+abs(hy-cy))
        sum_dist += min_dist
    return sum_dist


if __name__=="__main__":
    main()

