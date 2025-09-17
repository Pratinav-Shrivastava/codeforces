n, k = map(int, input().split())
nums = list(map(int, input().split()))

th = nums[k - 1]
ans = sum(1 for x in nums if x > 0 and x >= th)
print(ans)
