from math import gcd

t = int(input())
for _ in range(t):
    a, b, k = map(int, input().split())
    g = gcd(a, b)
    print(1 if a // g <= k and b // g <= k else 2)