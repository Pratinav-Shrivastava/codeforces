def main(nums):
    sum = 0
    for num in nums:
        sum += num
    print("YES" if sum%2 == 0 else "NO")

t = int(input())
for _ in range(t):
    input()
    nums = list(map(int, input().split()))
    main(nums)