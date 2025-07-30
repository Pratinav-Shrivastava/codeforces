for _ in range(int(input())):
    input()
    nums = list(map(int, input().split()))
    curr = 0
    final = 0
    for num in nums:
        if num == 0:
            curr += 1
            final = max(curr, final)
        else:
            curr = 0
    print(final)