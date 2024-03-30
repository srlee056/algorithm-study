def solution(n, k):
    
    k_num = ten_to_k(n, k)
    print("k_num", k_num)
    k_num += '0'
    pointer = 0
    result = []
    has_zero = False
    for i in range(len(k_num)):
        if k_num[i] == '0':
            has_zero = True
            str = k_num[pointer:i]
            pointer = i+1
            if str and is_prime(int(str)):
                result.append(str)
    if not has_zero:
        if is_prime(int(k_num)):
            result.append(k_num)
    #print(result)
    answer = len(result)
    return answer

def ten_to_k(n, k):
    if k == 10:
        return str(n)
    
    result = ''
    while n:
        result += (str(n%k))
        n = n //k
    
    return result[::-1]

def is_prime(n):
    
    if n <= 1:
        return False
    
    for i in range(2, int(n **0.5)+1):
        if n % i == 0:
            return False
    
    return True