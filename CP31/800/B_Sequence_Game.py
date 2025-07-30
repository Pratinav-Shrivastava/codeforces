def main(nums):
    result = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            result.append(1)
        result.append(nums[i])
    return result
    
t = int(input())
for _ in range(t):
    input()
    nums = list(map(int, input().split()))
    result = main(nums)
    print(len(result))
    print(*result)