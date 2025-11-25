n = int(input())
nums = list(map(int, input().split()))
given = 0
max_burles = max(nums)
for num in nums:
    if num != max_burles:
        given += max_burles - num
print(given)