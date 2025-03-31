def sieve(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False  # 0과 1은 소수가 아님

    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False

    return prime

m, n = map(int, input().split())
prime = sieve(n)  # n까지 소수 여부 계산

# m 이상 n 이하의 소수 출력
for i in range(m, n + 1):
    if prime[i]:
        print(i)