for _ in range(int(input())):
    input()
    nums = list(map(int, input().split()))

    count = 0
    # if len(nums) == 1:
    #     print(0)

    for i in range(len(nums)-1):
        if nums[i]%2 == nums[i+1]%2:
            count += 1
    print(count)