def solve():
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        left_coins = list(map(int, input().split()))
        right_coins = list(map(int, input().split()))
        
        count = 0
        for b in left_coins:
            for c in right_coins:
                if b + c <= k:
                    count += 1
        
        print(count)

if __name__ == "__main__":
    solve()