basic_price = int(input())
flower_1_price = int(input())
flower_2_price = int(input())
flower_1_num = int(input())
flower_2_num = int(input())
discount_bar = int(input())

total = basic_price + flower_1_num * flower_1_price + flower_2_num * flower_2_price

total_num = flower_1_num + flower_2_num + 2 if total >= discount_bar else flower_1_num + flower_2_num

print(total_num,total,sep=',')