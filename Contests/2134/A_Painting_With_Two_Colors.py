def painting(n, a, b):
    if a <= b:
        valid = (n-b)%2 == 0
    else:
        valid = (n-a)%2 == 0 and (n-b)%2 == 0
    return("YES" if valid else "NO")
    
    # blue_in_center = ((n - b) & 1) == 0
    # red = (a <= b) or (((a - b) & 1) == 0)
    # return("YES" if blue_in_center and red else "NO")

t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    print(painting(n, a, b))