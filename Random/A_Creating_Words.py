def swap(a, b):
    new_a = b[0] + a[1:]
    new_b = a[0] + b[1:]
    return(new_a, new_b)

t = int(input())
for _ in range(t):
    a, b = input().split()
    print(*swap(a, b))