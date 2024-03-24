def get_best_discount_customer(cus_nums, discount_nums, prob_list, left_cnt, cus_list):
    best_discount = 99999
    best_customer = 99999
    best_left_cnt = -1
    best_prob = -1
    for i in range(cus_nums):
        if cus_list[i] != 0:
            continue
        else:
            for j in range(discount_nums + 1):
                if left_cnt[j] > 0:
                    if prob_list[i][j] > best_prob:
                        best_discount = j
                        best_customer = i
                        best_prob = prob_list[i][j]
                        best_left_cnt = left_cnt[j]
                    elif prob_list[i][j] == best_prob:
                        if best_left_cnt < left_cnt[j]:
                            best_discount = j
                            best_customer = i
                            best_left_cnt = left_cnt[j]
                        elif best_left_cnt == left_cnt[j] and best_discount > j:
                            best_discount = j
                            best_customer = i
                            best_left_cnt = left_cnt[j]
    return best_customer, best_discount


nums = [int(i) for i in input().split(",")]
cus_nums, discount_nums = nums
prob_list = []

for i in range(cus_nums):
    probs = [int(i) for i in input().split(",")]
    prob_list.append(probs)

left_cnt = [cus_nums] + [int(i) for i in input().split(",")]

cus_list = [0 for _ in range(cus_nums)]

while 0 in cus_list:
    best_cus, best_dis = get_best_discount_customer(
        cus_nums, discount_nums, prob_list, left_cnt, cus_list
    )
    cus_list[best_cus] = str(best_dis)
    left_cnt[best_dis] -= 1

print(",".join(cus_list))
