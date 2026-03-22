table = input().strip()
hand = input().strip().split()

table_rank, table_suit = table[0], table[1]

for card in hand:
    if card[0] == table_rank or card[1] == table_suit:
        print("YES")
        break
else:
    print("NO")