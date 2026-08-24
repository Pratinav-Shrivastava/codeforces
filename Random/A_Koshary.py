t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    print("YES" if x % 2 == 0 or y % 2 == 0 else "NO")
