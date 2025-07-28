def main(x, s):
    res = 0
    while s not in x:
        x += x
        res +=1
        if res == 6:
            res = -1
            break
    return resgit 

for _ in range(int(input())):
    input()
    x = input()
    s = input()
    print(main(x, s))