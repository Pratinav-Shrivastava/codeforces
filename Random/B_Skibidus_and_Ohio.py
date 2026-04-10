def tc():
    s = input()
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            print(1)
            return
    print(len(s))

T = int(input())
for _ in range(T):
    tc()