def main(nums, x):
    max_distance = 0
    for i in range(1, len(nums)):
        max_distance = max(max_distance, nums[i] - nums[i-1])

    return max(max_distance, 2*(x-nums[-1]), nums[0])



t = int(input())
for _ in range(t):
    n, x =  map(int, input().split())
    nums = list(map(int, input().split()))

    print(main(nums, x))