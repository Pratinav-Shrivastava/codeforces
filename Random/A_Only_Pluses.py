def banana(a, b, c):
    for i in range(5):
        least = min(a, b, c)
        if a == least:
            a += 1
        elif b == least:
            b += 1
        elif c == least:
            c += 1
    return a*b*c

def solve():
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().split())
        print(banana(a, b, c))

if __name__ == "__main__":
    solve()