input()
scores = input()
anton_score = scores.count("A")
danik_score = scores.count("D")

if anton_score > danik_score:
    print("Anton")
elif anton_score < danik_score:
    print("Danik")
else:
    print("Friendship")