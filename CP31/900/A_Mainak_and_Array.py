def mainak(nums):
    ans=max(nums[-1]-min(nums),max(nums)-nums[0])
    for i in range(len(nums)):
        ans=max(ans,nums[i-1]-nums[i])
    return(ans)

t = int(input())
for _ in range(t):
    input()
    nums = list(map(int, input().split()))
    print(mainak(nums))