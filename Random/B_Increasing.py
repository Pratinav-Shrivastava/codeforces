t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    print("YES" if len(set(nums)) == n else "NO")
