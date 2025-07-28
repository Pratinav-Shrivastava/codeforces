def main(nums):
    if nums[0] == 1 and len(nums) != 0:
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    main(nums)