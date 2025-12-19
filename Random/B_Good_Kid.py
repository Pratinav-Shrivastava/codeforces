import math

t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    smallest = min(nums)
    product = 1
    done = False
    for num in nums:
        if num == smallest and not done:
            product *= (num+1)
            done = True
        else:
            product *= num
    print(product)
    