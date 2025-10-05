input()
nums = list(map(int, input().split()))
print("HARD" if nums.count(1) >= 1 else "EASY")