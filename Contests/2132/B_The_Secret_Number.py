def main(n):
    ans = []
    d = 11
    while d <= n:
        if n%d == 0:
            ans.append(n//d)
        d = 10*d - 9
    if not ans:
        print(0)
    else:
        ans.sort()
        print(len(ans))
        print(*ans)


t = int(input())
for _ in range(t):
    n = int(input())
    main(n)