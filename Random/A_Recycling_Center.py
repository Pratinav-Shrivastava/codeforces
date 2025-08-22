def main(c, weights):
    weights.sort()
    max_char = 0
    for i in range(len(weights)-1, -1, -1):
        if 1 <= weights[i] <= c:
            weights[i] = 0
            weights[:] = [x * 2 for x in weights]
    count = 0
    for element in weights:
        if element >= 1:
            count += 1
    return count


t = int(input())
for _ in range(t):
    n, c = map(int, input().split())
    weights = list(map(int, input().split()))
    print(main(c, weights))