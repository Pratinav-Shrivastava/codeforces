t = int(input())
for _ in range(t):
    a = input().strip()
    if a.startswith("10") and len(a) > 2 and a[2] != '0' and int(a[2:]) >= 2:
        print("YES")
    else:
        print("NO")