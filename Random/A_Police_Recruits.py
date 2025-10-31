n = int(input())
crimes_and_police = list(map(int, input().split()))
policemen, crimes = 0, 0
for event in crimes_and_police:
    if event == -1:
        if policemen > 0:
            policemen -= 1
            continue
        else:
            crimes += 1
    else:
        policemen += event
print(crimes)