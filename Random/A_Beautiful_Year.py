given = int(input())
given += 1
while len(set(str(given))) != len(str(given)):
    given += 1
print(given)