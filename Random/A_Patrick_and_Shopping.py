d1, d2, d3 = map(int, input().split())

ans = min(
    2 * (d1 + d2),
    2 * (d1 + d3),
    2 * (d2 + d3),
    d1 + d2 + d3
)

print(ans)
