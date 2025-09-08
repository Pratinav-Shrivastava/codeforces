def letter_home(n, s, x):
    x_min = x[0]
    x_max = x[n - 1]
    path1 = abs(s - x_min) + abs(x_max - x_min)
    path2 = abs(s - x_max) + abs(x_max - x_min)
    return(min(path1,path2))

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    x = list(map(int, input().split()))
    print(letter_home(n, s, x))