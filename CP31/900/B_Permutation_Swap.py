import math

def main(nums):
    k = abs(nums[0] - 1)
    for i in range(len(nums)):
        k = math.gcd(k, abs(nums[i] - (i+1)))
    return k

t = int(input())
for _ in range(t):
    input()
    nums = list(map(int, input().split()))
    print(main(nums))