code = input()
ans = []
i = 0
while i < len(code):
    if code[i] == ".":
        ans.append('0')
        i += 1
    elif code[i] == "-":
        if code[i+1] == ".":
            ans.append('1')
        elif code[i+1] == "-":
            ans.append('2')
        i += 2
print("".join(ans))