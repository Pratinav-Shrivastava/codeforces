def main():
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        s=0
        for i in range(n):
            s+=abs(arr[i])
        print(s)

main()