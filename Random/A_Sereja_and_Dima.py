n = int(input().strip())
cards = list(map(int, input().split()))

l, r = 0, n - 1
sereja = dima = 0
turn_sereja = True

while l <= r:
    if cards[l] >= cards[r]:
        take = cards[l]
        l += 1
    else:
        take = cards[r]
        r -= 1

    if turn_sereja:
        sereja += take
    else:
        dima += take
    turn_sereja = not turn_sereja

print(sereja, dima)