def main(s, k):
    odd_count = odd_counter(s)
    if k == 0 and odd_count <= 1:
        return("YES")
    else:
        if odd_count <= 1 or k >= odd_count or (k < odd_count and odd_count - k <= 1):
            return("YES")
        else:
            return("NO")

def odd_counter(s):
    hashmap = {}
    for letter in s:
        if letter in hashmap:
            hashmap[letter] += 1
        else:
            hashmap[letter] = 1
    
    count = 0
    for letter in hashmap:
        if hashmap[letter]%2 == 1:
            count += 1
    return count

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    print(main(s, k))
