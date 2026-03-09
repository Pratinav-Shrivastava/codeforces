def moves(a, b):
    if a == b:
        return 0
    elif a < b:
        if (b - a) % 2 == 1:
            return(1)
        else:
            return(2)
    else:
        if (a - b) % 2 == 0:
            return(1)
        else:
            return(2)

def solve():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        print(moves(a, b))

if __name__ == "__main__":
    solve()