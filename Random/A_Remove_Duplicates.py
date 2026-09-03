n = int(input())
a = list(map(int, input().split()))

seen = set()
ans = []

for x in reversed(a):
    if x not in seen:
        seen.add(x)
        ans.append(x)

ans.reverse()

print(len(ans))
print(*ans)