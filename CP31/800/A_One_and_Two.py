for _ in range(int(input())):
    input()
    nums = list(map(int, input().split()))
    result, two_count = 0, 0
    for num in nums:
        if num == 2:
            two_count += 1
    if two_count&1:
        print(-1)
    else:
        if two_count == 0:
            print(1)
        else:
            n = two_count/2
            two_twos = 0
            i = 0
            while two_twos < n:
                if nums[i] == 2:
                    two_twos += 1
                i += 1
            print(i)