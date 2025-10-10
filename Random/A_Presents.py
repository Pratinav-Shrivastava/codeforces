n = int(input())
g = list(map(int, input().split()))
ans = [0] * n
for giver, receiver in enumerate(g, start = 1):
    ans[receiver -1] = giver
print(*ans)