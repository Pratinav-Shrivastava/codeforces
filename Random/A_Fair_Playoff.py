t = int(input())
for _ in range(t):
    s1, s2, s3, s4 = map(int, input().split())
    
    final1 = max(s1, s2)
    final2 = max(s3, s4)
    
    skills = sorted([s1, s2, s3, s4])
    
    if final1 in skills[-2:] and final2 in skills[-2:]:
        print("YES")
    else:
        print("NO")
