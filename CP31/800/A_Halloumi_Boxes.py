class Solution:
    def canSort(self, nums, k):
        if k == 1 and not self.is_sorted(nums):
            return False
        return True

    def is_sorted(self, nums):
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                return False
        return True


def main():
    t = int(input())
    sol = Solution()
    for _ in range(t):
        n, k = map(int, input().split())
        nums = list(map(int, input().split()))
        if sol.canSort(nums, k):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()