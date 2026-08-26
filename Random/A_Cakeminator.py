R, C = map(int, input().split())

bad_rows = set()
bad_cols = set()

for i in range(R):
    row = input().strip()
    for j, ch in enumerate(row):
        if ch == 'S':
            bad_rows.add(i)
            bad_cols.add(j)

answer = R * C - len(bad_rows) * len(bad_cols)

print(answer)
