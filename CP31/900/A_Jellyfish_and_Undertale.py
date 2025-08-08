def main(a, b, tools):
    t = 0
    for tool in tools:
        if tool >= a:
            t += a - 1
        else:
            t += tool
    sum = t + b
    return sum

t = int(input())
for _ in range(t):
    a,b,_ = map(int, input().split())
    tools = list(map(int, input().split()))
    answer = main(a, b, tools)
    print(answer)