def odd_sum_possible(nums):
    total = sum(nums)
    if total&1:
        return("YES")
    else:
        return("YES" if any(n&1 for n in nums) and any(not n&1 for n in nums) else "NO")

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        print(odd_sum_possible(nums))

if __name__ == "__main__":
    solve()