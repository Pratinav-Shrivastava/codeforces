y, w = map(int, input().split())
a = max(y, w)
if a == 1:
    prob = "1/1"
elif a == 2:
    prob = "5/6"
elif a == 3:
    prob = "2/3"
elif a == 4:
    prob = "1/2"
elif a == 5:
    prob = "1/3"
elif a == 6:
    prob = "1/6"

print(prob)