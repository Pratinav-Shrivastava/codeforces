n, k = map(int, input().split())
time_remaining = 60*4
time_remaining -= k
i = 1
while time_remaining - 5*i >= 0 and i <= n:
    time_remaining -= 5*i
    i += 1
print(i-1)