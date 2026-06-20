def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    k = sum(a) // n
    for i in range(n - 1):
        if a[i] < k:
            print('NO')
            return
        a[i + 1] += a[i] - k
        a[i] = k
    print('YES')
    
    
for _ in range(int(input())):
    solve()