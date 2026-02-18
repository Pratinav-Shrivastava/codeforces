def make_it_white(n, s):
    left, right = 0, n - 1
    while s[left] != "B":
        left += 1
    while s[right] != "B":
        right -= 1
    stripe_length = right - left + 1
    return stripe_length

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(make_it_white(n, s))