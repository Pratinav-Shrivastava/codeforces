def timur_check(s, n):
    if n != 5:
        return "NO"
    return "YES" if set(s) == set("Timur") else "NO"

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    print(timur_check(s, n))
