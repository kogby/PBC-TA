choice_nums = int(input())
reds = [0] + [int(i) for i in input().split(",")]
yellow = [0] + [int(i) for i in input().split(",")]
white = [0] + [int(i) for i in input().split(",")]
price = [0] + [int(i) for i in input().split(",")]
bar_red = [int(i) for i in input().split(",")]
bar_yellow = [int(i) for i in input().split(",")]
bar_white = [int(i) for i in input().split(",")]


best_price_H = 9999999999
best_price_L = 9999999999
found_H = False
found_L = False
for i in range(choice_nums):
    for j in range(choice_nums):
        if (
            reds[i] + reds[j] >= bar_red[0]
            and yellow[i] + yellow[j] >= bar_yellow[0]
            and white[i] + white[j] >= bar_white[0]
        ):
            if price[i] + price[j] < best_price_H:
                best_price_H = price[i] + price[j]
                found_H = True
        if (
            not found_H
            and reds[i] + reds[j] >= bar_red[1]
            and yellow[i] + yellow[j] >= bar_yellow[1]
            and white[i] + white[j] >= bar_white[1]
        ):
            if price[i] + price[j] < best_price_L:
                best_price_L = price[i] + price[j]
                found_L = True

if found_H:
    print(best_price_H)
elif found_L:
    print(best_price_L)
else:
    total = 0
    for i in price:
        total += i
    print(total)
