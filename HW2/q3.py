happy_red = int(input())
happy_white = int(input())
happy_yellow = int(input())
true_red = int(input())
true_white = int(input())
true_yellow = int(input())
criteria_1 =int(input())
criteria_2 = int(input())
criteria_3 = int(input())
budget = int(input())

happy_price , true_price = 800, 1000
budget_allow = 0
feasible_min = 99999999
no_feasible = True

for happy_num in range(0, budget // happy_price + 1):
    for true_num in range(0, budget // true_price + 1):
        # Check whether the cost exceeds budget or not
        if true_num * true_price + happy_num * happy_price <= budget:
            budget_allow += 1

            # Check feasibility
            if (happy_red * happy_num + true_red * true_num >= criteria_1 or
            (happy_white + happy_yellow) * happy_num + (true_white + true_yellow) * true_num >= criteria_2 or
            (happy_red * 3 + happy_white) * happy_num + (true_red * 3 + true_white) * true_num >= criteria_3):
                total = happy_num * happy_price + true_num * true_price
                feasible_min = total if total < feasible_min else feasible_min
                no_feasible = False

# if no feasible solution, output -1
if no_feasible:
    feasible_min = -1
print(budget_allow,',',feasible_min,sep='')
