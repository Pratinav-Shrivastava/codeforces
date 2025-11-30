n, k = map(int, input().split())
ys = list(map(int, input().split()))

eligible = sum(1 for y in ys if y <= 5 - k)
print(eligible // 3)
