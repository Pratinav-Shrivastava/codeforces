t = int(input())
for _ in range(t):
    n = int(input())
    strengths = list(map(int, input().split()))

    strengths.sort()

    ans = float('inf')
    for i in range(n-1):
        ans = min(ans, strengths[i+1] - strengths[i])
    
    print(ans)