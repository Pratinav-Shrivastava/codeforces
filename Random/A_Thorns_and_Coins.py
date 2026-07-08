t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    ans = 0
    for i in range(1, n):
        if s[i] == '@':
            ans += 1
        if s[i] == '*' and s[i - 1] == '*':
            break

    print(ans)