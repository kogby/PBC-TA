nums = [int(i) for i in input().split(",")]
cus_nums, discount_nums = nums
prob_list = []

for i in range(cus_nums):
    probs = [int(i) for i in input().split(",")]
    prob_list.append(probs)

left_cnt = [cus_nums] + [int(i) for i in input().split(",")]
target = [int(i) for i in input().split(",")]

best_discount = 99999
best_customer = 99999
best_left_cnt = -1
best_prob = -1
for i in range(cus_nums):
    if target[i] != 1:
        for j in range(discount_nums + 1):
            if left_cnt[j] > 0:
                if prob_list[i][j] > best_prob:
                    best_discount = j
                    best_customer = i + 1
                    best_prob = prob_list[i][j]
                    best_left_cnt = left_cnt[j]
                elif prob_list[i][j] == best_prob:
                    if best_left_cnt < left_cnt[j]:
                        best_discount = j
                        best_customer = i + 1
                        best_left_cnt = left_cnt[j]
                    elif best_left_cnt == left_cnt[j] and best_discount > j:
                        best_discount = j
                        best_customer = i + 1
                        best_left_cnt = left_cnt[j]

print(best_customer, best_discount, sep=",")
