t = int(input())
for _ in range(t):
    n = int(input())
    vec = list(map(int, input().split()))
    print(max(vec) * n)