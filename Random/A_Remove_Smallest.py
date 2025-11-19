def remove_smallest(n, nums):
    if n == 1:
        return "YES"
    nums.sort()
    for i in range(1, n):
        if nums[i] - nums[i-1] > 1:
            return "NO"
    return "YES"
    

t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    print(remove_smallest(n, nums))