n = int(input())
contest_ratings = list(map(int, input().split()))
amazing_count = 0
all_time_best = all_time_worst = contest_ratings[0]

for i in range(1, n):
    curr = contest_ratings[i]
    if curr > all_time_best:
        amazing_count += 1
        all_time_best = curr
    elif curr < all_time_worst:
        amazing_count += 1
        all_time_worst = curr
print(amazing_count)