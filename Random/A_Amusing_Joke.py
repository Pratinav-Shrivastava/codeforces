from collections import Counter

guest = input().strip()
host = input().strip()
pile = input().strip()

need = Counter(guest + host)
have = Counter(pile)

print("YES" if need == have else "NO")