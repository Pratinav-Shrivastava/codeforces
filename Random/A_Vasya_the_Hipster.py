a, b = map(int, input().split())
fashionable = min(a,b)
same = (max(a,b) - fashionable)//2
print(fashionable, same)