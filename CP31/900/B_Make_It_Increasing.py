def make_strictly_increasing(nums):
    ans = 0
    for i in range(len(nums)-2, -1, -1):
        while nums[i] >= nums[i+1]:
            ans += 1
            nums[i] = nums[i]//2
            if nums[i] == 0:
                break
        if nums[i] == 0 and nums[i+1] == 0:
            return -1
    return ans 

t = int(input())
for _ in range(t):
    input()
    nums = list(map(int, input().split()))
    print(make_strictly_increasing(nums))