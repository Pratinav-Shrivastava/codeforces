n = int(input())
m_points = c_points = 0
for _ in range(n):
    m, c = map(int, input().split())
    if m > c:
        m_points += 1
    if m < c:
        c_points += 1
    
if m_points == c_points:
    print("Friendship is magic!^^")
else:
    print("Mishka" if m_points > c_points else "Chris")