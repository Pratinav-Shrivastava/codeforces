n = int(input())
teams = list(map(int, input().split()))

prog, math, pe = [], [], []

for i, x in enumerate(teams, start=1):
    if x == 1: prog.append(i)
    elif x == 2: math.append(i)
    else: pe.append(i)

w = min(len(prog), len(math), len(pe))
print(w)

for i in range(w):
    print(prog[i], math[i], pe[i])
