t = int(input())

for _ in range(t):
    n = input().strip()

    if int(n[-1]) % 2 == 0:
        print(0)
    elif int(n[0]) % 2 == 0:
        print(1)
    elif any(d in n for d in "2468"):
        print(2)
    else:
        print(-1)