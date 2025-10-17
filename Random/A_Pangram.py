n = int(input())
s = input()
ans = set(s.lower())
print("YES" if len(ans) >= 26 else "NO")