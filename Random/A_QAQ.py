s = input()
n = len(s)

prefix_Q = [0] * n
count = 0
for i in range(n):
    prefix_Q[i] = count
    if s[i] == 'Q':
        count += 1

suffix_Q = [0] * n
count = 0
for i in range(n-1, -1, -1):
    suffix_Q[i] = count
    if s[i] == 'Q':
        count += 1

result = 0
for i in range(n):
    if s[i] == 'A':
        result += prefix_Q[i] * suffix_Q[i]

print(result)