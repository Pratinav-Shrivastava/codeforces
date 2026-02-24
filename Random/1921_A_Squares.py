def solve():
    t = int(input())
    for _ in range(t):
        xs = []
        ys = []
        
        for _ in range(4):
            x, y = map(int, input().split())
            xs.append(x)
            ys.append(y)
        
        side = max(xs) - min(xs)
        print(side * side)


if __name__ == "__main__":
    solve()