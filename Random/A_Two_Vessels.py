t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    d=abs(a-b)
    if d==0:
        print(0)
    else:
        print((d + 2*c - 1) // (2*c))