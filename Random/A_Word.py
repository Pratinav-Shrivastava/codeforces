s = input()
upper = sum(c.isupper() for c in s)
lower = sum(c.islower() for c in s)

print(s.upper() if upper > lower else s.lower())