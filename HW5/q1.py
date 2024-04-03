def best_product_info(item_cnt, minutes, prices):
   best_index, second_best_index = -1, -1
   best_cp, second_cp = -1, -1
   cp_list = [prices[i]/minutes[i] for i in range(item_cnt)]
   for ind, cp in enumerate(cp_list):
        if cp > best_cp:
            second_cp  = best_cp
            second_best_index = best_index
            best_cp = cp
            best_index = ind + 1
        elif cp > second_cp:
            second_cp = cp
            second_best_index = ind + 1

   return best_index, second_best_index


# input
item_cnt, capacity_1 , capacity_2 = [int(x) for x in input().split(",")]
minutes = [int(x) for x in input().split(",")]
prices = [int(x) for x in input().split(",")]

# call function and calculate the answer
best_index, second_best_index = best_product_info(item_cnt, minutes, prices)
revenue = prices[best_index-1] * (capacity_1//minutes[best_index-1]) + prices[second_best_index-1] * (capacity_2//minutes[second_best_index-1])

# print
print(best_index, second_best_index, revenue, sep = ",")