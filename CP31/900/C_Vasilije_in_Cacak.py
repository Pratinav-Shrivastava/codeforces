def main(n, k, x):
    return (k * (k + 1) / 2) <= x <= (n*(n+1) / 2) - ((n-k)*(n-k+1) / 2)

t = int(input())
for _ in range(t):
    n, k, x = map(int, input().split())
    result = main(n, k, x)
    print("YES" if result else "NO")