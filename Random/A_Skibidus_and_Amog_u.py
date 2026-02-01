t = int(input())
for _ in range(t):
    singular_word = input()
    plural_word = singular_word[:-2] + "i"
    print(plural_word)