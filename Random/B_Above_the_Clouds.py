t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    cnt = [0] * 26
    for c in s:
        cnt[ord(c) - ord('a')] += 1

    flag = False
    for i in range(26):
        if cnt[i] >= 3:
            flag = True
        elif cnt[i] == 2 and (ord(s[0]) - ord('a') != i or ord(s[-1]) - ord('a') != i):
            flag = True

    print("Yes" if flag else "No")