a = input()
b = input()
result = []
for i in range(len(a)):
    result.append(int(a[i])^int(b[i]))
ans = ''.join(str(ch) for ch in result)
print(ans)


# s1 = input()
# s2 = input()
# ans = []
# for i in range(len(s1)):
#     if s1[i] == s2[i]:
#         ans.append(0)
#     else:
#         ans.append(1)
# result = ''.join(str(a) for a in ans)
# print(result)