n, m = map(int, input().split())

ans = 0
for a in range(1001):
    b = n - a*a
    if b < 0:
        break
    if a + b*b == m:
        ans += 1

print(ans)