def odd_one_out(a, b, c):
    if a != b:
        return b if a == c else a
    else:
        return c

t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    print(odd_one_out(a, b, c))