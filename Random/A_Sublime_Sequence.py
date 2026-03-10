t = int(input())
for _ in range(t):
    x, n = map(int, input().split())
    print(x if n&1 else 0)