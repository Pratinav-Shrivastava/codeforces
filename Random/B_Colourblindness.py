t = int(input())

for _ in range(t):
    n = int(input())
    row1 = input().replace('G', 'B')
    row2 = input().replace('G', 'B')
    
    print("YES" if row1 == row2 else "NO")
