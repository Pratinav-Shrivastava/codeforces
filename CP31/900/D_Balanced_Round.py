def main(nums, n, k):
    nums.sort()
    if n <= 1:
        return 0
    
    bw = 1
    ans = 1    
    for i in range(1, n):
        if nums[i] - nums[i-1] > k:
            bw = 1
        else:
            bw += 1
        ans = max(ans, bw)
    return n - ans

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    print(main(nums, n, k))