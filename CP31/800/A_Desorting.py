def main(nums):
    if is_sorted(nums):
        min_gap = float('inf')
        for i in range(1, len(nums)):
            min_gap = min(min_gap, abs(nums[i] - nums[i-1]))
        return((min_gap//2) + 1)
    else:
        return 0

def is_sorted(nums):
    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] < 0:
            return False
    return True

t = int(input())
for _ in range(t):
    input()
    nums = list(map(int, input().split()))
    print(main(nums))
    # print(is_sorted(nums))