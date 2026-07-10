t = int(input())

for _ in range(t):
    n, m, x, y = map(int, input().split())

    # Read n integers
    if n > 0:
        list(map(int, input().split()))

    # Read m integers
    if m > 0:
        list(map(int, input().split()))

    print(n + m)