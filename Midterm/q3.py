nums = [int(i) for i in input().split(",")]
n, target = nums

candidate_nums = [int(i) for i in input().split(",")]
count = 0

for i in range(n):
    for j in range(i + 1, n):
        if candidate_nums[i] * candidate_nums[j] == target:
            count += 1

print(count)
