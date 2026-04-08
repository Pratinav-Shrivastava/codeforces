t = int(input())
for _ in range(t):
    s = input()
    print("YES" if s.count('B') * 2 == len(s) else "NO")