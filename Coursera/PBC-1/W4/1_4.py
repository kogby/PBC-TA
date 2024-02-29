cost = int(input())
price = int(input())
max_demand = int(input())
quant = 0

esti_revenue = 0
for i in range(max_demand + 1):
    prob = float(input())
    if i <= quant:
        esti_revenue += prob * (price * i - quant * cost)
    else:
        esti_revenue += prob * (price * quant - quant * cost)  # If reach maximum of bought quantity
    # print(esti_revenue)
print(int(esti_revenue))
