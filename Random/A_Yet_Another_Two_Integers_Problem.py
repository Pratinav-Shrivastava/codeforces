t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    d = abs(a - b)
    print((d + 9) // 10)  