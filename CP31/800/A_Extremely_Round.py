# def main(n):
    # a = x = 1
    # res = 0
    # while x <= n:
    #     for i in range(1, 10):
    #         x = a * i
    #         if x > n:
    #             break
    #         res += 1
    #     a *= 10
    # print("log is ", log(n))
    # print(res)

def main(n):
    d = len(str(n))
    answer =  9 * (d - 1) + n // 10**(d - 1)
    print(answer)

t = int(input())
for _ in range(t):
    n = int(input())
    main(n)
