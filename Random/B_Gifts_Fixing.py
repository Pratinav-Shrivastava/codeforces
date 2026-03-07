def equalize_gifts(n, a, b):
    minA = min(a)
    minB = min(b)

    moves = 0
    for i in range(n):
        moves += max(a[i] - minA, b[i] - minB)
    return moves

def solve():
    t = int(input())

    for _ in range(t):
        n = int(input().strip())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(equalize_gifts(n, a, b))

if __name__ == "__main__":
    solve()