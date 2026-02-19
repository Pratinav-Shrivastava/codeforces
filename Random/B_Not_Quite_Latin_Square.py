def latin_square(matrix):
    for row in matrix:
        if "?" in row:
            for ch in "ABC":
                if ch not in row:
                    return ch

t = int(input())
for _ in range(t):
    matrix = [input() for _ in range(3)]
    
    print(latin_square(matrix))