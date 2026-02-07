import math

t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    
    total = sum(nums)
    root = int(math.isqrt(total))
    
    print("YES" if root*root == total else "NO")