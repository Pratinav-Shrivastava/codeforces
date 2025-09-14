def long_words(word):
    if len(word) <= 10:
        return word
    result = [word[0], str(len(word)-2), word[-1]]
    answer = "".join(result)
    return answer

t = int(input())
for _ in range(t):
    word = input()
    print(long_words(word))