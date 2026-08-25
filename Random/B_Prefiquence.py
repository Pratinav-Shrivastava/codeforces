t = int(input())

while t:
    t -= 1

    n, m = map(int, input().split())
    a = input()
    b = input()

    dp = [0] * (m + 1)

    dp[1] = 1 if a[0] == b[0] else 0

    for i in range(2, m + 1):
        if dp[i - 1] != n and b[i - 1] == a[dp[i - 1]]:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = dp[i - 1]

    print(dp[m])
