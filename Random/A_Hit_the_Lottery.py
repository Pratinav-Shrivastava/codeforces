n = int(input())
ans = 0
for d in (100, 20, 10, 5, 1):
    ans += n // d
    n %= d
print(ans)