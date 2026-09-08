t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    cnt1 = arr.count(1)
    print(n - cnt1 // 2)
