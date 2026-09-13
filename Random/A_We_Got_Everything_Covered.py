tc = int(input())

for _ in range(tc):
    n, k = map(int, input().split())
    print(''.join(chr(ord('a') + i) for i in range(k)) * n)
