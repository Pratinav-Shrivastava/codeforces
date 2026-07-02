def solve():
    n, d = map(int, input().split())
    s = input()
    
    for i in range(n):
        if int(s[i]) >= d:
            print(s[i], end="")
        else:
            print(d, end="")
            print(s[i:])
            return
    print(d)


t = int(input())
for _ in range(t):
    solve()