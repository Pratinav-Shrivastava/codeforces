t = int(input())

for _ in range(t):
    s = input().strip()
    hh, mm = s.split(":")
    h = int(hh)

    if h == 0:
        h12 = 12
        period = "AM"
    elif 1 <= h < 12:
        h12 = h
        period = "AM"
    elif h == 12:
        h12 = 12
        period = "PM"
    else:
        h12 = h - 12
        period = "PM"

    print(f"{h12:02d}:{mm} {period}")