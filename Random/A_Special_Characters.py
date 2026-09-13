t = int(input())

for _ in range(t):
    n = int(input())

    if n % 2 == 1:
        print("NO")
        continue

    print("YES")

    result = []
    for i in range(n // 2):
        result.append("A" if i % 2 == 0 else "B")
        result.append("A" if i % 2 == 0 else "B")

    print("".join(result))
