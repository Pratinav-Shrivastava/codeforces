def main(n):
    if n%3 == 0:
        print("Second")
    else:
        print("First")

t = int(input())
for _ in range(t):
    main(int(input()))