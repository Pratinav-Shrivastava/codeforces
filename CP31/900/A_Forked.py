def main(knight_moves, king_position, queen_position):
    # return(knight_moves, king_position, queen_position)
    dx, dy = knight_moves
    deltas = knight_deltas(dx, dy)
    king_vulnerable = attack_from(king_position, deltas)
    queen_vulnerable = attack_from(queen_position, deltas)

    return (len(king_vulnerable & queen_vulnerable))

def knight_deltas(a,b):
    if a == b:
        return [(a,b), (-a,-b), (a,-b), (-a,b)]
    else:
        return[(a,b), (a,-b), (-a, b), (-a,-b),
                (b,a), (-b, a), (b, -a), (-b, - a)]

def attack_from(pos, deltas):
    x, y = pos
    attack = set()
    for dx, dy in deltas:
        attack.add((x + dx, y + dy))
    return attack

t = int(input())
for _ in range(t):
    knight_moves = list(map(int, input().split()))
    king_position = list(map(int, input().split()))
    queen_position = list(map(int, input().split()))
    print(main(knight_moves, king_position, queen_position))