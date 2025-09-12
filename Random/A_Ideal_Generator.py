def ideal_generator(k):
    if k&1:
        return("YES")
    else:
        return("NO")

t = int(input())
for _ in range(t):
    k = int(input())
    print(ideal_generator(k))