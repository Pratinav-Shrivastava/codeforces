t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    sm = 0
    for ch in s:
        sm += 1 if ch == '+' else -1

    print(abs(sm))