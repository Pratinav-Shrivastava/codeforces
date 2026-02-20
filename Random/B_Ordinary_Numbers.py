def ordinary_numbers(n):
    count = 0
    for i in range(1, 10):
        num = i
        while num <= n:
            count += 1
            num = num *10 + i
    return count

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(ordinary_numbers(n))

if __name__ == "__main__":
    solve()