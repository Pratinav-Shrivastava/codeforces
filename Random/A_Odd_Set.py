t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    odds, evens = 0, 0
    for num in nums:
        if num&1: 
            odds += 1
        else:
            evens += 1
    
    print("Yes" if odds == evens else "No")