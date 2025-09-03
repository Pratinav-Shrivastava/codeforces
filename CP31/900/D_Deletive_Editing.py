from collections import Counter

def deletive(s, t):
    freq_map = dict(Counter(t))
    s_word = list(s)
    # print(s_word)
    # print(freq_map)
    for i in range(len(s_word)-1, -1, -1):
            if s_word[i] in freq_map:
                freq_map[s_word[i]] -= 1
                if freq_map[s_word[i]] == 0:
                    del freq_map[s_word[i]]
            else:
                s_word[i] = "."
    # print(s_word)
    result = []
    for j in range(len(s_word)):
        if s_word[j] != ".":
            # print(s_word[j])
            result.append(s_word[j])
    final_word = "".join(result)
    # print(final_word)
    return("YES" if final_word == t else "NO")

t = int(input())
for _ in range(t):
    s, t = input().split()
    print(deletive(s, t))