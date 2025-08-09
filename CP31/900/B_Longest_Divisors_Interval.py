def main(n):
    i = 1
    while (n%i == 0):
        i += 1
    return i - 1

t = int(input())
for _ in range(t):
    n = int(input())
    print(main(n))