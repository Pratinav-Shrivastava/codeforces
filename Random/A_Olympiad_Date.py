def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        cnt = [0] * 10
        f = False
        for i in range(n):
            cnt[a[i]] += 1
            if cnt[0] >= 3 and cnt[1] >= 1 and cnt[2] >= 2 and cnt[3] >= 1 and cnt[5] >= 1 and not f:
                print(i + 1)
                f = True
        if not f:
            print(0)

solve()