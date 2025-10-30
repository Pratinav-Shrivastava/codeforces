x1, x2, x3 = map(int, input().split())
ans = max(x1, x2, x3) - min(x1, x2, x3)
print(ans)