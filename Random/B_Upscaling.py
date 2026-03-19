t = int(input())
for _ in range(t):
    n = int(input())
    size = 2 * n
    board = [['.' for _ in range(size)] for _ in range(size)]
    
    for block_row in range(n):
        for block_col in range(n):
            char = '#' if (block_row + block_col) % 2 == 0 else '.'
            r_start, c_start = block_row*2, block_col*2
            for r in range(r_start, r_start+2):
                for c in range(c_start, c_start+2):
                    board[r][c] = char

    for row in board:
        print(''.join(row))