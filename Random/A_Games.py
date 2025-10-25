from collections import Counter

t = int(input())
homes, aways = [], []

for _ in range(t):
    h, a = map(int, input().split())
    homes.append(h)
    aways.append(a)

away_freq = Counter(aways)
ans = sum(away_freq[h] for h in homes)
print(ans)