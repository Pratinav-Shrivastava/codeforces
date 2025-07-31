def main(n,a,b):
    if n == a == b:
        return("Yes")
    else:
        return("Yes" if n-a-b>=2 else "No")

t = int(input())
for _ in range(t):
    n,a,b = map(int,input().split())
    print(main(n,a,b))