def solution(n):
    answer = [[]]
    #1~n-1 from #1 to #2, n #1 to #3, 1~n-1 from #2 to #3
    answer = move(n, 1, 3, 2)
    return answer

def move(n, start, end, left):
    if n == 1:
        return [[start, end]]
    
    result = move(n-1, start, left, end)
    result = result + move(1, start, end, end)
    result = result + move(n-1, left, end, start)
    
    return result
    
    
    