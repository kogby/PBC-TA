basic_price = int(input())
flower_1_price = int(input())
flower_2_price = int(input())
flower_1_num = int(input())
flower_2_num = int(input())
discount_bar_1 = int(input())
discount_bar_2 = int(input())
price_range_floor = int(input())
price_range_ceil = int(input())

total = basic_price + flower_1_num * flower_1_price + flower_2_num * flower_2_price
total_num = flower_1_num + flower_2_num

if total >= discount_bar_2:
    total_num += 5
elif total >= discount_bar_1:
    total_num += 2

if price_range_floor <= total <= price_range_ceil:
    total = price_range_floor

print(total_num, total, sep=",")
