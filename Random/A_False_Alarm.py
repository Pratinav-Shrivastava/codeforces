def false_alarm(n, x, doors):
    l, r = float("inf"), -1
    for i in range(n):
        door = doors[i]
        if door == 1:
            l = min(l, i)
            r = max(r, i)
    return("YES" if x >= r-l+1 else "NO")

t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    doors = list(map(int, input().split()))
    print(false_alarm(n, x, doors))