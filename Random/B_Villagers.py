def grumpy_villagers(nums):
    sorted_nums = sorted(nums, reverse = True)
    total = 0
    for i in range(0, len(nums), 2):
        total += sorted_nums[i]
    return total

t = int(input())
for _ in range(t):
    input()
    nums = list(map(int, input().split()))
    print(grumpy_villagers(nums))