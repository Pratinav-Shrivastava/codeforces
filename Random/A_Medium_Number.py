t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    medium = 0
    if a > b and a > c:
        medium = b if b > c else c
    if b > a and b > c:
        medium = a if a > c else c
    if c > a and c > b:
        medium = a if a > b else b
    print(medium)