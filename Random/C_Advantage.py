t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    
    max1 = max(s)
    max2 = max(x for x in s if x != max1) if s.count(max1) == 1 else max1
    
    res = []
    for x in s:
        if x == max1:
            res.append(x - max2)
        else:
            res.append(x - max1)
    
    print(*res)