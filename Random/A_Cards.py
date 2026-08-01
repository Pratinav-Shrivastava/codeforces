n = int(input())
s = input()

ans = ["1"] * s.count('n') + ["0"] * s.count('z')
print(*ans)