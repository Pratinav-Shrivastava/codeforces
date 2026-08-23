t = int(input())

while t:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))

    mini = min(max(a[i], a[i + 1]) for i in range(n - 1))

    print(mini - 1)
