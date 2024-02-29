cost = int(input())
price = int(input())
max_demand = int(input())
prob_list = []
for p in range(max_demand+1):
    prob_list.append(float(input()))

best_revenue = -999
best_quant = -1
for quant in range(max_demand+1):
    esti_revenue = 0
    for i in range(max_demand + 1):
        if i <= quant:
            esti_revenue += prob_list[i] * (price * i - quant * cost)
        else:
            esti_revenue += prob_list[i] * (price * quant - quant * cost)  # If reach maximum of bought quantity
        # print(esti_revenue)
    if best_revenue < esti_revenue:
        best_revenue = esti_revenue
        best_quant = quant

print(best_quant, int(best_revenue))
