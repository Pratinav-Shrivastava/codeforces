n, k, l, c, d, p, nl, np = map(int, input().split())

total_ml = k * l
total_slices = c * d
total_salt = p

toasts_by_drink = total_ml // (n * nl)
toasts_by_limes = total_slices // n
toasts_by_salt  = total_salt // (n * np)

print(min(toasts_by_drink, toasts_by_limes, toasts_by_salt))
