n, k = map(int, input().split())

originalN = n
# n을 2진수로 바꿨을 때 1의 숫자 = 합쳤을 때 물병의 최소 숫자
cnt = 0
# n 2진수 모드에서 1 개수를 세서 k보다 작게 될 때까지
# 그때까지 n에 더해준 숫자만큼 물병을 사면 됨 
while bin(n).count('1') > k:
    n = n+1
    
print(n - originalN)