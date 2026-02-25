import math

def tower_of_boxes(n, m, d):
    if m > d:
        return n
    else:
        max_tower = 1 + d//m
        if max_tower >= n:
            return 1
        else:
            return math.ceil(n / max_tower)

def solve():
    t = int(input())
    for _ in range(t):
        n, m, d = map(int, input().split())
        print(tower_of_boxes(n, m, d))

if __name__ == "__main__":
    solve()