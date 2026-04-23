def remove_xs(n, file_name):
    cnt = 0
    remove_count = 0
    
    for char in file_name:
        if char == 'x':
            cnt += 1
            if cnt >= 3:
                remove_count += 1
        else:
            cnt = 0
    
    return remove_count

n = int(input())
file_name = input()

result = remove_xs(n, file_name)
print(result)