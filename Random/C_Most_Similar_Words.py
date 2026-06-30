def cost(a, b):
    val = 0
    for i in range(len(a)):
        val += abs(ord(a[i]) - ord(b[i]))
    return val


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    s = [input().strip() for _ in range(n)]

    ans = float('inf')

    for i in range(n):
        for j in range(i + 1, n):
            ans = min(ans, cost(s[i], s[j]))

    print(ans)