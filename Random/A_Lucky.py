t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    half = n // 2
    left_sum  = sum(int(c) for c in s[:half])
    right_sum = sum(int(c) for c in s[half:])
    lucky = (left_sum == right_sum)
    print("YES" if lucky else "NO")
