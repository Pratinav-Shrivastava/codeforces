n = int(input())
nums = list(map(int, input().split()))
min_idx, max_idx = 0, n-1
min_num, max_num = float("inf"), float("-inf")

for idx, value in enumerate(nums):
    if value <= min_num:
        min_num = value
        min_idx = max(idx, min_idx)
    if value > max_num:
        max_num = value
        max_idx = idx

ans = (n - min_idx - 1) + (max_idx)
if max_idx > min_idx:  
    ans -= 1
print(ans)