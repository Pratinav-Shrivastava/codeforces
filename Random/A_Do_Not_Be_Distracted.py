t = int(input())
for _ in range(t):
    n = int(input())
    tasks = input()
    seen = set()
    prev = None
    suspicious = False
    
    for ch in tasks:
        if ch != prev:
            if ch in seen:
                suspicious = True
                break
            seen.add(ch)
            prev = ch
    
    print("NO" if suspicious else "YES")