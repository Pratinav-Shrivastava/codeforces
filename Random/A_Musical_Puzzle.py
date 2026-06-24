def solve():
    n = int(input())
    s = input()
    cnt = set()
    for i in range(1, n):
        cnt.add(s[i - 1] + s[i])
    print(len(cnt))


t = int(input())
for _ in range(t):
    solve()