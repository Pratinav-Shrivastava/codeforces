def main():
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())
        if ((a ^ b) & 1):
            print("NO")
        else:
            print("YES")

if __name__ == "__main__":
    main()