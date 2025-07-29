def main(nums):
    total = 0
    for i in nums:
        total += i
    print(total*(-1))

t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    main(nums)