n = int(input())
s = input().strip()

index = 0
gap = 1

while index < n:
    print(s[index], end="")
    index += gap
    gap += 1