n = int(input())
level_set = set()
x = list(map(int, input().split()))
y = list(map(int, input().split()))

for i in range(1, len(x)):
    level_set.add(x[i])
for j in range(1, len(y)):
    level_set.add(y[j])

print("I become the guy." if n == len(level_set) else "Oh, my keyboard!")