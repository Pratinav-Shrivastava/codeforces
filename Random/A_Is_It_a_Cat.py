def solve():
    n = int(input())
    s = input().lower()
    t = s[0]
    for c in s[1:]:
        if c != t[-1]:
            t += c
    print("YES" if t == "meow" else "NO")

for _ in range(int(input())):
    solve()