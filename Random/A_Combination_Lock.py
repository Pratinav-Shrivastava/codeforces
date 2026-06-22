n = int(input())
s = input().strip()
t = input().strip()

ans = 0

for i in range(n):
    d = abs(int(s[i]) - int(t[i]))
    ans += min(d, 10 - d)

print(ans)