def lever(list1, list2):
    return sum(a-b for a, b in zip(list1, list2) if a > b) + 1

t = int(input())
for _ in range(t):
    input()
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))
    print(lever(list1, list2))