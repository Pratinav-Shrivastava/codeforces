def main(s):
    ans = 1
    streak = 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            streak += 1
        else:
            streak = 1
        ans = max(ans, streak+1)
    return max(ans, streak+1)

t = int(input())
for _ in range(t):
    input()
    s = input()
    print(main(s))