t = int(input())

for _ in range(t):
    a, b = input().split()

    ca = a[-1]
    cb = b[-1]

    if ca == cb:
        if len(a) == len(b):
            print("=")
        elif ca == "S":
            print(">" if len(a) < len(b) else "<")
        else:
            print("<" if len(a) < len(b) else ">")
    else:
        print(">" if ca < cb else "<")