def main(nums):
    nums.sort()
    max_num = nums[-1]
    c = []
    b = []
    for num in nums:
        if num == max_num:
            c.append(num)
        else:
            b.append(num)
    return (b,c)

t = int(input())
for _ in range(t):
    input()
    nums = list(map(int, input().split()))
    b,c = main(nums)
    if len(b) == 0:
        print(-1)
    else:
        print(*(len(b), len(c)))
        print(*b)
        print(*c)
        