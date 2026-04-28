def solve():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(1, n):
        if abs(a[i] - a[i - 1]) != 5 and abs(a[i] - a[i - 1]) != 7:
            return False
    return True

t = int(input())
for _ in range(t):
    print("YES" if solve() else "NO")