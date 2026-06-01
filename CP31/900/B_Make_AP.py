def make_ap(a, b, c):
    if (2*b - c) > 0 and (2*b - c) % a == 0:
        return "YES"
    if (a + c) % 2 == 0:
        b_target = (a + c) // 2
        if b_target % b == 0:
            return "YES"
    if (2*b - a) > 0 and (2*b - a) % c == 0:
        return "YES"
    
    return "NO"

def main():
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().split())
        print(make_ap(a, b, c))

if __name__ == "__main__":
    main()