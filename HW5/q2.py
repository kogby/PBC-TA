def within_budget(i, j, price_happiness, price_heart, budget):
    is_within_budget = True
    if (i * price_happiness + j * price_heart > budget):
        is_within_budget = False
    return is_within_budget


def meet_one_req(i, j, happy_flower, heart_flower, price_happiness, price_heart, budget, requirement):
    total_price = i * price_happiness + j * price_heart
    total_r, total_w, total_y = [i * happy_flower[k] + j * heart_flower[k] for k in range(3)]
    if total_r >= requirement[0] or total_w + total_y >= requirement[1] or total_r * 3 + total_w >= requirement[2]:
        return total_price
    else:
        return budget + 1
  


# input
red_happiness = int(input())
white_happiness = int(input())
yellow_happiness = int(input())
red_heart = int(input())
white_heart = int(input())
yellow_heart = int(input())
K1 = int(input())
K2 = int(input())
K3 = int(input())
budget = int(input())
price_happiness = 800
price_heart = 1000

A1 = budget // price_happiness + 1 
A2 = budget // price_heart + 1
min_price = budget + 1
num_of_strategies_within_budget = 0

heart_flower = [red_heart,white_heart,yellow_heart]
happy_flower = [red_happiness,white_happiness,yellow_happiness]
requirement = [K1,K2,K3]

for i in range(A1): # happiness
    for j in range(A2): # heart
        if within_budget(i, j, price_happiness, price_heart, budget):
            num_of_strategies_within_budget += 1            
            price = meet_one_req(i, j, happy_flower, heart_flower, price_happiness, price_heart, budget, requirement)
            if price < min_price:
                min_price = price

if min_price >  budget:
    print(str(num_of_strategies_within_budget) + ",-1")
else:
    print(num_of_strategies_within_budget, min_price, sep=",")
