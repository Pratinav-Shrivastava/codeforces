from collections import Counter

def name_possible(s, t):
    return("YES" if Counter(s) == Counter(t) else "NO")

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s, t = input().split()
        print(name_possible(s, t))

if __name__ == "__main__":
    solve()