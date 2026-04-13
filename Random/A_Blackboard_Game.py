def solve():
    n=int(input())
    print("Alice" if n%4 else "Bob")

t=int(input())
for _ in range(t):
    solve()