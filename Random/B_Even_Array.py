def even_array(nums):
    a, b = 0, 0
    for i in range(len(nums)):
        if i % 2 != nums[i] % 2:
            if  i % 2 == 0:
                a += 1
            else:
                b += 1
    if a != b:
        return -1
    else:
        return a

t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    print(even_array(nums))