def rectangles(l1, b1, l2, b2, l3, b3):
    if (l1 + l2 + l3) == b1 and b1 == b2 and b2 == b3:
        return "YES"
    elif (l2 + l3) == l1 and b2 == b3 and (b1 + b2) == l1:
        return "YES"
    elif (b1 + b2 + b3) == l1 and l1 == l2 and l2 == l3:
        return "YES"
    elif (b2 + b3) == b1 and l2 == l3 and (l1 + l2) == b1:
        return "YES"
    else:
        return "NO"

t = int(input())
for _ in range(t):
    l1, b1, l2, b2, l3, b3 = map(int, input().split())
    print(rectangles(l1, b1, l2, b2, l3, b3))
