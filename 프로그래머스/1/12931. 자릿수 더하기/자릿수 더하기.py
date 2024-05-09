def solution(n):
    sum_ = 0
    while n > 0 :
        sum_ += n % 10
        n = n // 10
    
    #print(sum)

    return sum_