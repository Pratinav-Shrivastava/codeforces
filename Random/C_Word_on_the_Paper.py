def main(arr):
    answer = []
    for i in range(len(arr)):
        for char in arr[i]:
            if char != ".":
                answer.append(char)
    return "".join(answer)

t = int(input())
for _ in range(t):
    arr = [list(input()) for _ in range(8)]
    # print(arr)
    print(main(arr))