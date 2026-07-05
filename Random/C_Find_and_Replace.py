def solve():
    n = int(input())
    s = input().strip()

    mp = [-1] * 26

    for i in range(n):
        curr = ord(s[i]) - ord('a')
        if mp[curr] == -1:
            mp[curr] = i % 2
        else:
            if mp[curr] != i % 2:
                print("NO")
                return

    print("YES")


t = int(input())
for _ in range(t):
    solve()