total = 0
t = int(input())
for _ in range(t):
    curr_statement = input()
    if curr_statement[1] == "+":
        total += 1
    else:
        total -= 1
print(total)
    
