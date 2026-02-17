t = int(input())
for _ in range(t):
    a = input()
    
    mapping = {"p":"q", "q":"p"}
    result = "".join(mapping.get(ch, ch) for ch in reversed(a))

    print(result)