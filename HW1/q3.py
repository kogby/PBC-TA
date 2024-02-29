flower_1_need = int(input())
flower_2_need = int(input())
set_1_f1 = int(input())
set_1_f2 = int(input())
set_1_price = int(input())
set_2_f1 = int(input())
set_2_f2 = int(input())
set_2_price = int(input())

set_1_buy = False
set_2_buy = False

if flower_1_need <= set_1_f1 and flower_2_need <= set_1_f2:
    set_1_buy = True
if flower_1_need <= set_2_f1 and flower_2_need <= set_2_f2:
    set_2_buy = True

if not set_1_buy and not set_2_buy:
    total = set_1_price + set_2_price
    total_num = set_1_f1 + set_1_f2 + set_2_f1 + set_2_f2
elif set_1_buy and set_2_buy:
    if set_1_price <= set_2_price:
        total = set_1_price
        total_num = set_1_f1 + set_1_f2
    else:
        total = set_2_price
        total_num = set_2_f1 + set_2_f2
elif set_1_buy:
    total = set_1_price
    total_num = set_1_f1 + set_1_f2
else:
    total = set_2_price
    total_num = set_2_f1 + set_2_f2

print(total_num, total, sep=",")
