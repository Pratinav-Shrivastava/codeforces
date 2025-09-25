n = int(input())
s = input()

consecutive_count = 0
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        consecutive_count += 1
print(consecutive_count)