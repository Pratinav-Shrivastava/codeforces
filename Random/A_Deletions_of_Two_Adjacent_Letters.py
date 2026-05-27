t = int(input())
for _ in range(t):
    s = input().strip()
    t_str = input().strip()
    yes = False
    for i in range(len(s)):
        if s[i] == t_str[0] and i % 2 == 0:
            yes = True
    print("YES" if yes else "NO")