cnt = 0
a1, a2, a3, a4 = map(int, input().split())
s = input()
for num in s:
    if num == '1':
        cnt += a1
    elif num == '2':
        cnt += a2
    elif num == '3':
        cnt += a3
    elif num == '4':
        cnt += a4
print(cnt)