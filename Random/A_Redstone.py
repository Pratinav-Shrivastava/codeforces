def redstone(nums):
    if len(nums) == 2:
        if nums[0] == nums[1]:
            return "YES"
        return "NO"
    else:
        return ("YES" if len(set(nums)) < len(nums) else "NO")

t = int(input())
for _ in range(t):
    input()
    nums = list(map(int, input().split()))
    print(redstone(nums))