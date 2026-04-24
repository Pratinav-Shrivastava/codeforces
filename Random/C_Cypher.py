def solve():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        parts = input().split()
        b = int(parts[0])
        if b == 0:
            continue
        now = parts[1]
        for j in range(b):
            if now[j] == 'U':
                a[i] -= 1
            else:
                a[i] += 1
            if a[i] < 0:
                a[i] += 10
            if a[i] > 9:
                a[i] -= 10
    print(*a)

t = int(input())
for _ in range(t):
    solve()