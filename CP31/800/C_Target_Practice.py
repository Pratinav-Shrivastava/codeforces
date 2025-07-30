def main(arr):
    n = 10
    score = 0
    for i in range(n):
        for j in range(n):
            # print("We will take minimum of: ", i,j, n-i-1, n-j-1)
            layer = min(i, j, n-1-i, n-1-j) + 1
            if arr[i][j] == "X":
                score += layer
    print(score)    
    
t = int(input())
for _ in range(t):
    final_array = []
    for x in range(10):
        line = list(input())
        # print(line)
        final_array.append(line)
    # print(final_array)
    main(final_array)

