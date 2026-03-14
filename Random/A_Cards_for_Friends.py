def can_cut(w, h, n):
    pieces = 1
    while w % 2 == 0:
        w //= 2
        pieces *= 2
    while h % 2 == 0:
        h //= 2
        pieces *= 2
    return pieces >= n

t = int(input())
for _ in range(t):
    w, h, n = map(int, input().split())
    if can_cut(w, h, n):
        print("YES")
    else:
        print("NO")