t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print("Alice" if (a+b)&1 else "Bob")