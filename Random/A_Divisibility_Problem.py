def answer(a, b):
    count = a%b
    return(0 if count == 0 else b - count)

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(answer(a, b))