t = int(input())
for _ in range(t):
    ancient_name = input().split()
    modern_name = "".join(word[0] for word in ancient_name)
    print(modern_name)