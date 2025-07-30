for _ in range(int(input())):
    input()
    nums = list(map(int, input().split()))
    negative_count, positive_count = 0, 0
    for num in nums:
        if num == -1:
            negative_count += 1
        else:
            positive_count += 1
    result = 0
    while (negative_count&1) or (negative_count > positive_count):
        result += 1
        negative_count -= 1
        positive_count += 1
    print(result)
