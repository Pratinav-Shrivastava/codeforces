t = int(input())

for _ in range(t):
    k = int(input())
    acc = 0
    hv = False

    nums = []
    while len(nums) < k:
        nums.extend(map(int, input().split()))

    for x in nums[:k]:
        acc += x
        if x % 3 == 1:
            hv = True

    if acc % 3 == 0:
        print(0)
    elif acc % 3 == 2:
        print(1)
    else:
        print(1 if hv else 2)