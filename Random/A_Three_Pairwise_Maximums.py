t=int(input())
for _ in range(t):
    x,y,z=map(int,input().split())
    a=[x,y,z]
    a.sort()
    if a[1]!=a[2]:
        print("NO")
    else:
        print("YES")
        print(a[0],a[0],a[2])