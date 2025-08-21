def main(a, b, c):
    end = list(a)
    start = []
    for i in range(len(c)):
        if c[i] == "D":
            end.append(b[i])
        elif c[i] == "V":
            start.append(b[i])
    start.reverse()
    final = "".join(start) + "".join(end)
    return final

t = int(input())
for _ in range(t):
    input()
    a = input()
    input()
    b = input()
    c = input()
    print(main(a, b, c))