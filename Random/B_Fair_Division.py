t = int(input())
for _ in range(t):
    n = int(input())
    candies = list(map(int, input().split()))
    ones = candies.count(1)
    twos = candies.count(2)

    total = ones + 2 * twos
    
    if total % 2 != 0:
        print("NO")
    else:
        target = total // 2
        
        if target % 2 == 1 and ones == 0:
            print("NO")
        else:gi
            print("YES")