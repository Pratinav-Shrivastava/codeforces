def buses(n):
    if n&1 or n < 4:
        print("-1")
        return
    minimum = n//6 if n%6 == 0 else n//6 + 1
    maximum = n // 4
    print(minimum, maximum)
    

t = int(input())
for _ in range(t):
    n = int(input())
    buses(n)