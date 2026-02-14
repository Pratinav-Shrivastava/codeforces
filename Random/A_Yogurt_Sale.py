t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    
    ans = a
    if 2*a <= b:
        ans = n*a
    else:
        if n & 1:
            ans = ((n-1)//2)*b + a
        else:
            ans = (n//2) * b
    
    print(ans)