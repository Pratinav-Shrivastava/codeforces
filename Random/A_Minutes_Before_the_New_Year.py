t = int(input())
for _ in range(t):
    h, m = map(int, input().split())
    minutes_left = 60*(23-h) + (60-m)
    print(minutes_left)