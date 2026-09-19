n = int(input())

bus = [input() for _ in range(n)]

found = False

for i in range(n):
    if bus[i][0:2] == "OO":
        bus[i] = "++" + bus[i][2:]
        found = True
        break

    elif bus[i][3:5] == "OO":
        bus[i] = bus[i][:3] + "++"
        found = True
        break

if found:
    print("YES")
    for row in bus:
        print(row)
else:
    print("NO")
