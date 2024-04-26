import sys
from collections import defaultdict, deque

def main():
    n, m = map(int,sys.stdin.readline().split())

    for row in backtrack(n, m):
        print(' '.join(map(str, row)))


def backtrack(n, m):
    if m == 1:
        return [[i] for i in range(1,n+1)]
    
    result = []
    prev_lists = backtrack(n, m-1)
    for list_ in prev_lists:
        for i in range(1,n+1):
            result.append(list_+[i])
    
    return result
    



if __name__=="__main__":
    main()

