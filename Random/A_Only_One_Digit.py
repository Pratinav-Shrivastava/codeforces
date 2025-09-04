def one_digit(stringed_number):
    temp = set()
    for i in range(len(stringed_number)):
        temp.add(int(stringed_number[i]))
    result = min(temp)
    return result

t = int(input())
for _ in range(t):
    stringed_number = input()
    print(one_digit(stringed_number))