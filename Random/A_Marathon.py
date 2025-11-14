t = int(input())
for _ in range(t):
    a, b, c, d = map(int, input().split())
    count = (b>a) + (c>a) + (d>a)
    print(count)