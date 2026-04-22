t = int(input())
pi = '31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
for _ in range(t):
    n = input() + '#'
    for i in range(len(n)):
        if pi[i] != n[i]:
            print(i)
            break