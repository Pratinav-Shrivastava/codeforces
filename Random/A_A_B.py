t = int(input())
for _ in range(t):
    expression = input()
    result = 0
    for ch in expression:
        if ch != "+":
            result += int(ch)
    print(result)