def main(a, b, c):
    if a+b >= 10 or a+c >= 10 or b+c >= 10:
        return("YES")
    else:
        return("NO")

t = int(input())
for _ in range(t):
    a, b, c =list(map(int, input().split()))
    print(main(a, b, c))