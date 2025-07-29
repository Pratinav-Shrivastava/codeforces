def main(nums, k):
    if k in nums:
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    n_and_k = list(map(int, input().split()))
    n = n_and_k[0]
    k = n_and_k[1]
    nums = list(map(int, input().split()))
    # print(n, k)
    # print("nums is: ", nums)
    main(nums, k)