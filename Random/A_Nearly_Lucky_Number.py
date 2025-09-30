n = input()
count = 0
for num in n:
    if num == "4" or num == "7":
        count +=1
print("YES" if count == 4 or count == 7 else "NO")
