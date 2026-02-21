def LCM_Problem(l, r):
    result = ()
    if l*2 > r:
        result = -1, -1
    else:
        result = l, l*2
    return result

def solve():
    t = int(input())
    for _ in range(t):
        l, r = map(int, input().split())
        x, y = LCM_Problem(l,r)
        print(x, y)

if __name__ == "__main__":
    solve()