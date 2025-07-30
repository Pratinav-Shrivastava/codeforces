for _ in range(int(input())):
    sx, sy, dx, dy = map(int, input().split())
    # print(sx, sy, dx, dy)
    moves = 0
    if dy < sy:
        print(-1)
        # continue
    else:
        moves = dy - sy
        sx += moves
        if sx < dx:
            print(-1)
            # continue
        else:
            moves += sx - dx
            print(moves)