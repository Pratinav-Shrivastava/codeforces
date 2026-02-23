import math

def carnival_wheel(l, a, b):
    g = math.gcd(l,b)
    return l - g + (a%g)
    
    # biggest = a
    # seen = set()
    # while a not in seen:
    #     seen.add(a)
    #     a = (a + b) % l
    #     biggest  = max(a, biggest)
    # return biggest

def solve():
    t = int(input())
    for _ in range(t):
        l, a, b = map(int, input().split())
        print(carnival_wheel(l, a, b))

if __name__ == "__main__":
    solve()