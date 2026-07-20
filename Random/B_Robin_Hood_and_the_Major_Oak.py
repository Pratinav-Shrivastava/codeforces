t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    if n % 2 == 1:
        odd = (k + 1) // 2
    else:
        odd = k // 2

    if odd % 2 == 0:
        print("YES")
    else:
        print("NO")