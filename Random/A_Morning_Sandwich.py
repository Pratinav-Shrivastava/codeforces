def main():
    for _ in range(int(input())):
        b, c, h = map(int, input().split())
        print(min(b - 1, c + h) * 2 + 1)

if __name__ == "__main__":
    main()