red = int(input())
white = int(input())
yellow = int(input())
criteria_1 = int(input())
criteria_2 = int(input())
criteria_3 = int(input())

count = 1
while True:
    if red * count >= criteria_1:
        break
    if (white + yellow) * count >= criteria_2:
        break
    if (red * 3 + white) * count >= criteria_3:
        break
    count += 1

print(count)
