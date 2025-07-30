for _ in range(int(input())):
    n = int(input())
    str = input()
    i, j = 0, len(str) - 1
    result = n
    while i < j and result > 0:
        if str[i] != str[j]:
            result -= 2
            i += 1
            j -= 1
        else:
            break
    print(result)