import math

n, k = map(int, input().split())
T = 240 - k
if T <= 0:
    print(0)
else:
    # i = floor((-5 + sqrt(25 + 40*T)) / 10)
    i = ( -5 + math.sqrt(25 + 40*T) ) // 10  # integer-safe
    print(int(min(n, i)))

# n, k = map(int, input().split())
# time_remaining = 60*4
# time_remaining -= k
# i = 1
# while time_remaining - 5*i >= 0 and i <= n:
#     time_remaining -= 5*i
#     i += 1
# print(i-1)