import math

def prime(x: int) -> bool:
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    r = int(math.sqrt(x))
    for d in range(3, r + 1, 2):
        if x % d == 0:
            return False
    return True

def next_prime_is_m(n: int, m: int) -> str:
    for i in range(n + 1, m + 1):
        if prime(i):
            return "YES" if i == m else "NO"
    return "NO"

# If you want to read input and print the answer:
if __name__ == "__main__":
    n, m = map(int, input().split())
    print(next_prime_is_m(n, m))
