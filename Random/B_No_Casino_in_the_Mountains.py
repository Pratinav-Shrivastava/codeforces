def hikes_mountains(nums, k):
    hikes = 0
    consecutive_good_days = 0
    i = 0
    while i < len(nums):
        if nums[i] == 0:
            consecutive_good_days += 1
            if consecutive_good_days == k:
                hikes += 1
                consecutive_good_days = 0 
                i += 1
        else:
            consecutive_good_days = 0
        i += 1
    return hikes

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    print(hikes_mountains(nums, k))