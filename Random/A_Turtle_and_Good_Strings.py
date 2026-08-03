def solve():
    n= int(input())
    s = input()
    print("Yes" if s[0] != s[-1] else "No")


t = int(input())
for _ in range(t):
    solve()