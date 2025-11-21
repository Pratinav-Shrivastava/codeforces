def spy_detected(nums):
    if nums[0] == nums[1] or nums[0] == nums[2]:
        majority = nums[0]
    else:
        return 1

    for i, v in enumerate(nums, start = 1):
        if v != majority:
            return i

t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    print(spy_detected(nums))