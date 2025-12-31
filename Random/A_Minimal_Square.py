t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    
    side = min(
        max(2 * a, b),
        max(a, 2 * b)
    )
    
    print(side * side)