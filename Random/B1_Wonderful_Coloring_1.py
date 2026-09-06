t = int(input())

for _ in range(t):
    s = input().strip()

    cnt = [0] * 26

    for c in s:
        cnt[ord(c) - ord('a')] += 1

    cnt1 = 0
    cnt2 = 0

    for x in cnt:
        if x == 1:
            cnt1 += 1
        elif x > 0:
            cnt2 += 1

    print(cnt2 + cnt1 // 2)
