from collections import Counter

def main(nums):
    count = Counter(nums)
    # print(count)
    if len(count) > 2:
        return False
    if len(count) == 1:
        return True
    freq = list(count.values())
    # print(freq)
    return abs(freq[0] - freq[1]) <= 1
    


t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    print("Yes" if main(nums) else "No")