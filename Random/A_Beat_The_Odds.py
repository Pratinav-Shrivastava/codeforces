t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    num_odd = sum(x % 2 for x in a)

    print(min(num_odd, n - num_odd))