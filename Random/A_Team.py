def team(a,b,c):
    if a + b + c >= 2:
        return True
    
count = 0

t = int(input())
for _ in range(t):
    a, b, c, = map(int, input().split())
    count += 1 if team(a,b,c) else 0
print(count)