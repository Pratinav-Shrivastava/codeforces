def not_dividing(nums):
    for x in range(len(nums)):
        if nums[x] == 1:
            nums[x] += 1
            
    i = 0 
    while i < len(nums)-1:
        if nums[i+1] % nums[i] == 0:
            nums[i+1] += 1
        i += 1
    return nums

t = int(input())
for _ in range(t):
    input()
    nums = list(map(int, input().split()))
    print(*not_dividing(nums))