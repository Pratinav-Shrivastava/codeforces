t = int(input())
c = 'codeforces'
for _ in range(t):
    s = input()
    # if len(s) != len(c):
    #     print("NOPES")
    cnt = 0
    for i in range(len(c)):
        if c[i] != s[i]:
            cnt += 1
    print(cnt)    