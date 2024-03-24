nums = [int(i) for i in input().split(",")]
ppl_num, exp_criteria, pro_criteria, sum_criteria = nums

exp_list = [int(i) for i in input().split(",")]
pro_list = [int(i) for i in input().split(",")]
qualify_list = []
for i in range(ppl_num):
    if exp_list[i] >= exp_criteria and pro_list[i] >= pro_criteria:
        qualify_list.append(str(i + 1))

if len(qualify_list) == 0:
    for i in range(ppl_num):
        if exp_list[i] + pro_list[i] >= sum_criteria:
            qualify_list.append(str(i + 1))

if len(qualify_list) != 0:
    print(",".join(qualify_list))
else:
    print(0)
