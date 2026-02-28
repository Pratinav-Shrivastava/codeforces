def eating_game(dishes):
    most = max(dishes)
    eligible = dishes.count(most)
    return eligible

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        dishes = list(map(int, input().split()))
        print(eating_game(dishes))

if __name__ == "__main__":
    solve()