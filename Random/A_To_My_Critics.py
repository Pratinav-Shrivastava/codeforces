def main(a, b, c):
    return("YES" if ((a+b+c - min(a,b,c))>=10) else "NO")

t = int(input())
for _ in range(t):
    a, b, c =list(map(int, input().split()))
    print(main(a, b, c))