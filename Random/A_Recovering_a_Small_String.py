def solve():
    n = int(input())
    mins = "zzz"
    for i in range(26):
        for j in range(26):
            for k in range(26):
                if i + j + k + 3 == n:
                    cur = chr(i + ord('a')) + chr(j + ord('a')) + chr(k + ord('a'))
                    if cur < mins:
                        mins = cur
    print(mins)

t = int(input())
for _ in range(t):
    solve()