def smallest_distance(nums):
    nums.sort()
    median = nums[1]

    distance = sum(abs(x-median) for x in nums)
    return distance

def solve():
    t = int(input())
    for _ in range(t):
        nums = list(map(int, input().split()))
        print(smallest_distance(nums))

if __name__ == "__main__":
    solve()