def main(a, b, c):
    if c&1:
        print("First" if a >= b else "Second")
    else:
        print("First" if a > b else "Second" )

t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    main(a,b,c)