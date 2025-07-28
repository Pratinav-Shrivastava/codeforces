
def main(x):
    curr_dots = 0
    total_dots = 0
    for d in x:
        if d == '.':
            curr_dots += 1
            total_dots += 1
            if curr_dots == 3:
                return 2
        else:
            curr_dots = 0
    return total_dots


t = int(input())
for _ in range(t):
    n = int(input())
    x = input()
    print(main(x))