n = int(input())

if n % 2 == 0:
    k = n // 2
    print(k)
    print(" ".join(["2"] * k))
else:
    k = (n - 3) // 2 + 1
    print(k)
    print("3", end=" ")
    print(" ".join(["2"] * ((n - 3) // 2)))
