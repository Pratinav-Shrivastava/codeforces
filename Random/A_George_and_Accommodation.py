rooms = int(input())
ans = 0
for _ in range(rooms):
    p, q = map(int, input().split())
    if q - p >= 2:
        ans += 1
print(ans)