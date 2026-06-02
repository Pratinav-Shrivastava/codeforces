for i in range(int(input())):
    nums = list(map(int, input().split()))
    print(2 * max(nums) - sum(nums))