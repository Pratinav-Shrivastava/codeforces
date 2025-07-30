for _ in range(int(input())):
    input()
    nums = list(map(int, input().split()))
    result = []
    for num in nums:
        result.append(len(nums)+1 - num)
    print(*result)
