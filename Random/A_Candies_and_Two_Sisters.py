def no_of_ways(n):
    if n&1:
        return(n//2)
    else:
        return (n//2 - 1)


t = int(input())

for _ in range(t):
    n = int(input())
    print(no_of_ways(n))