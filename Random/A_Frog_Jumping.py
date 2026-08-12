t = int(input())

for _ in range(t):
    a, b, k = map(int, input().split())
    print((a - b) * (k // 2) + a * (k & 1))