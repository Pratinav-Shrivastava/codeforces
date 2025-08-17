def main(arr):
    ans = 1
    result = 1
    for i in range(len(arr)):
        # print("arr[i][0] is: ", arr[i][0])
        if arr[i][0] <= 10:
            if arr[i][1] > ans:
                ans = arr[i][1]
                result = i + 1
            # print("arr[i][1] would be: ", arr[i][1])
            # print("currently ans is: ", ans)
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for anything in range(n):
        key, value = map(int, input().split())
        arr.append((key,value))
    print(main(arr))