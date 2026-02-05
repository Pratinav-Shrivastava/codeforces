n = int(input())
nums = list(map(int, input().split()))

curr_len = 1
best_len = 1

for i in range(1, n):
    if nums[i] > nums[i - 1]:
        curr_len += 1
    else:
        curr_len = 1
    best_len = max(best_len, curr_len)

print(best_len)
