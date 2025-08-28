def thanos(nums):
    n = len(nums)
    any_nz = False
    for x in nums:
        if x != 0:
            any_nz = True
            break
    if not any_nz:
        return 0

    L = 0
    while L < n and nums[L] == 0:
        L += 1
    R = n - 1
    while R >= 0 and nums[R] == 0:
        R -= 1

    for i in range(L, R + 1):
        if nums[i] == 0:
            return 2
    return 1

t = int(input())
for _ in range(t):
    input()
    nums = list(map(int, input().split()))
    print(thanos(nums))