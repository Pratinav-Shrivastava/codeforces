def triple(n, nums):
    seen = {}
    for num in nums:
        seen[num] = seen.get(num, 0) + 1
        if seen[num] == 3:
            return num
    return -1


t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    print(triple(n, nums))