def main(modified_total_sum):
    return("YES" if modified_total_sum&1 else "NO")     

t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    nums = list(map(int, input().split()))
    
    total_sum = sum(nums)
    prefix_sum = [0]*(n+1)
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + nums[i]

    for _ in range(q):
        l, r, k = map(int, input().split())
        original_sub_sum = prefix_sum[r] - prefix_sum[l-1]
        new_sub_sum = (r-(l-1))*k
        modified_total_sum = total_sum - original_sub_sum + new_sub_sum
        print(main(modified_total_sum))
