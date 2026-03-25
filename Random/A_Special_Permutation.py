t = int(input())
for _ in range(t):
    n=int(input())
    p=list(range(1,n+1))
    if n%2==0:
        for i in range(0,n,2):
            p[i],p[i+1]=p[i+1],p[i]
    else:
        for i in range(0,n-3,2):
            p[i],p[i+1]=p[i+1],p[i]
        p[-3],p[-2],p[-1]=p[-2],p[-1],p[-3]
    print(*p)