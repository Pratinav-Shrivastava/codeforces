tc = int(input())

for _ in range(tc):
    n, k = map(int, input().split())

    A = [input().strip() for _ in range(n)]

    for i in range(0, n, k):
        print(''.join(A[i][j] for j in range(0, n, k)))