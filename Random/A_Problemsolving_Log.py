for _ in range(int(input())):
    n = int(input())
    s = input()
    print(sum([s.count(chr(ord('A') + i)) >= i + 1 for i in range(26)]))