def candy(nums):
    sum_evens = sum(x for x in nums if not x&1)
    sum_odds = sum(x for x in nums if x&1)
    
    return("YES" if sum_evens > sum_odds else "NO")

    # evens.sort(reverse=True)
    # odds.sort()

    # sum_evens, sum_odds = 0, 0
    # if sum(evens) <= sum(odds):
    #     return "NO"
    # for i in range(min(len(odds), len(evens))):
    #     sum_odds += odds[i]
    #     sum_evens += evens[i]
    #     if sum_odds >= sum_evens:
    #         return "NO"
    # return "YES"

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        print(candy(nums))

if __name__ == "__main__":
    solve()