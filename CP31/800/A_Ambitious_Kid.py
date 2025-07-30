def main(nums):
    closest_to_zero = float('inf')
    for element in nums:
        closest_to_zero = min(closest_to_zero, abs(element))
    return closest_to_zero

n = int(input())
nums = list(map(int, input().split()))
print(main(nums))