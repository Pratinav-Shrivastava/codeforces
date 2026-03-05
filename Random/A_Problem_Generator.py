def solve():
    t = int(input())
    
    for _ in range(t):
        n, m = map(int, input().split())
        s = input()
        
        freq = {c: 0 for c in "ABCDEFG"}
        
        for ch in s:
            freq[ch] += 1
        
        ans = 0
        for c in "ABCDEFG":
            if freq[c] < m:
                ans += m - freq[c]
        
        print(ans)

if __name__ == "__main__":
    solve()