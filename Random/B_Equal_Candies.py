t = int(input())
for _ in range(t):
    n = int(input())
    candies = list(map(int, input().split()))
    to_eat = 0
    lowest_box = min(candies)
    for candy in candies:
        to_eat += candy - lowest_box
    print(to_eat)