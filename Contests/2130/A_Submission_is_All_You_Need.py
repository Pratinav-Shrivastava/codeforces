def main(nums):
    zero_count = nums.count(0)
    return(sum(nums) + zero_count)

t = int(input())
for _ in range(t):
    input()
    nums = list(map(int, input().split()))
    print(main(nums))