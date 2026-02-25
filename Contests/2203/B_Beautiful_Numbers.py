def moves(n):
    digits = list(map(int, str(n)))
    s = sum(digits)
    
    if s <= 9:
        return 0
    
    excess = s - 9
    moves = 0

    indexed_digits = [(digits[i], i) for i in range(len(digits))]
    indexed_digits.sort(reverse=True)

    for d, idx in indexed_digits:
        if excess <= 0:
            break
        if idx == 0:
            max_reduction = d-1
        else:
            max_reduction = d
        if max_reduction <= 0:
            continue

        reduction = min(max_reduction, excess)
        excess -= reduction
        moves += 1
    
    return moves

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(moves(n))

if __name__ == "__main__":
    solve()