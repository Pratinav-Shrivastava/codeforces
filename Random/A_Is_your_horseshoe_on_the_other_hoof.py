from collections import Counter

nums = map(int, input().split())
ans = 4 - len(set(nums))
print(ans)