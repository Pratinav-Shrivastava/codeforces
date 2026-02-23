def food(a, b, c, x, y):
    need_x = max(0, x-a)
    need_y = max(0, y-b)
    return("YES" if need_x + need_y <= c else "NO")
    
    # if x <= a and y <= b:
    #     return("YES")
    # elif x <= a and y > b:
    #     return("YES" if b + c >= y else "NO")
    # elif x > a and y <= b:
    #     return("YES" if a + c >= x else "NO")
    # elif x > a and y > b:
    #     return("YES" if (a + b + c >= x + y) else "NO")

def solve():
    t = int(input())
    for _ in range(t):
        a, b, c, x, y = map(int, input().split())
        print(food(a,b,c,x,y))

if __name__ == "__main__":
    solve()