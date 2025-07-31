def main(nums):
    if max(nums) == min(nums):
        print("NO")
    else:
        print("YES")
        is_ugly = 0
        sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == sum:
                is_ugly = 1
                break
            else:
                sum += nums[i]
        if not is_ugly:
            print(*nums)
        else:
            nums[0], nums[-1] = nums[-1], nums[0]
            print(*nums)
        


t = int(input())
for _ in range(t):
    input()
    nums = list(map(int, input().split()))

    main(nums)
