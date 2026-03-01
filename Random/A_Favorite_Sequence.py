def restore(sequence):
    ans = []
    l, r = 0, len(sequence) - 1
    
    while l <= r:
        ans.append(sequence[l])
        if l != r:
            ans.append(sequence[r])
        l += 1
        r -= 1
    return ans

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        sequence = list(map(int, input().split()))
        print(*restore(sequence))

if __name__ == "__main__":
    solve()