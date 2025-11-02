t = int(input())
for _ in range(t):
    n = int(input())

    ans = []
    power = 1
    while n > 0:
        digit = n % 10
        if digit > 0:
            ans.append(digit * power)
        n //= 10
        power *= 10

    print(len(ans))
    print(*ans)