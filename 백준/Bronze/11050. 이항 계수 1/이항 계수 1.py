n, k = map(int, input().split())

n_mul, k_mul = 1, 1

for i in range(k):
    n_mul *= n - i
    k_mul *= k - i

print(n_mul // k_mul)
