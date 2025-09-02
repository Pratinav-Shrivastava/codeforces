def difficult_contest(s):
    ans = sorted(list(s), reverse=True)
    return "".join(ans)

t = int(input())
for _ in range(t):
    s = input()
    print(difficult_contest(s))