def max_monkeys_seated(m, a, b, c):
    row1_seated = min(a, m)
    row2_seated = min(b, m)
    remaining_row1 = m - row1_seated
    remaining_row2 = m - row2_seated
    remaining_monkeys = min(c, remaining_row1 + remaining_row2)
    return row1_seated + row2_seated + remaining_monkeys

t = int(input())
for _ in range(t):
    m, a, b, c = map(int, input().split())
    print(max_monkeys_seated(m, a, b, c))