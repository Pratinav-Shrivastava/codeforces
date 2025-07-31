import math

def main(nums):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if math.gcd(nums[i], nums[j]) <= 2:
                return "Yes"
    return "No"

t = int(input())
for _ in range(t):
    input()
    nums = list(map(int, input().split()))
    print(main(nums))