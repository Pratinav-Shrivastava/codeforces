def ugly(n, p):
    pos = p.index(1)
    p[pos], p[n-1] = p[n-1], p[pos]
    return p

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        p = list(map(int, input().split()))

        print(*ugly(n, p))

if __name__ == "__main__":
    solve()