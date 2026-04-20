t = int(input())
for _ in range(t):
    n = int(input())
    total_sum = 0
    a_list = list(map(int, input().split()))  
    for a in a_list:
        total_sum += a
    
    if total_sum < n:
        print(1)
    else:
        print(total_sum - n)