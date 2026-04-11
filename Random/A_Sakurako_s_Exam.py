t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    if a%2==1:
        print("NO")
        continue
    if a==0 and b%2==1:
        print("NO")
        continue
    print("YES")