from collections import deque
def solution(arr):
    biggest = sorted(arr)[-1]

    primes = get_primes(biggest)
    
    factors = {prime:0 for prime in primes}
    for num in arr:
        factorization(num, primes, factors)
        
    #print(factors)
    
    answer = 1
    for factor, count in factors.items():
        answer *= factor**count
    
    return answer

def get_primes(number):
    is_prime = [True for _ in range(number+1)]
    
    for i in range(2, int(number**0.5)+1):
        if is_prime[i]:
            #print(i)
            for j in range(i*2, number+1, i):
                is_prime[j] = False
    
    primes = [p for p in range(2, number+1) if is_prime[p]]
    #print(primes)
    return primes

def factorization(number, primes, factors):
    
    cur_num = number
    for prime in primes:
        if prime > number:
            break
        prime_count = 0
        while cur_num % prime == 0:
            cur_num = cur_num // prime
            prime_count += 1
        factors[prime] = max(factors[prime], prime_count)
            
    return 