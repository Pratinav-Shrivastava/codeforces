t = int(input())
for _ in range(t):
    x = input().strip()
    dig = int(x[0]) - 1
    length = len(x)
    print(dig * 10 + length * (length + 1) // 2)
