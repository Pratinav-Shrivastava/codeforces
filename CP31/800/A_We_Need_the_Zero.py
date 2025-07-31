def main(nums):
    total_xor = 0
    for num in nums:
        total_xor ^= num
    
    if(len(nums)%2 == 1):
        return total_xor
    else:
        if total_xor == 0:
            return total_xor
        else:
            return -1
    
t = int(input())
for _ in range(t):
    input()
    nums = list(map(int, input().split()))
    print(main(nums))