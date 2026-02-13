t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    x, y = 0, 0
    found = False
    
    for ch in s:
        if ch == "L":
            x -= 1
        if ch == "R":
            x += 1
        if ch == "U":
            y += 1
        if ch == "D":
            y -= 1

        if x == 1 and y == 1:
            found = True
            break
    
    print("YES" if found else "NO") 