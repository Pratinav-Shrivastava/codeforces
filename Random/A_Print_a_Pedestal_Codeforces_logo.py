import sys

def solve():
    n = int(sys.stdin.readline())
    for a in range(3, n):
        c = (n - a) // 2
        b = n - a - c
        if c > 1 and b + 1 < a:
            c -= 1
            b += 1
        if a > b > c:
            sys.stdout.write(f"{b} {a} {c}\n")
            return

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()