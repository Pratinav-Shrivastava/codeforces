def perfect_permutation(n):
    res = []
    for i in range(1, n+1, 2):
        res.append(i+1)
        res.append(i)
    return res

def solve():
    n = int(input())
    if n&1:
        print(-1)
    else:
        print(*perfect_permutation(n))

if __name__ == "__main__":
    solve()