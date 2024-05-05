store_num, non_available = map(int, input().split(","))
store = list(map(float, input().split(",")))
no_build = []
if non_available != 0:
    no_build = list(map(int, input().split(",")))

for i in range(store_num):
    if len(no_build) != 0 and i + 1 in no_build:
        continue
    total = 0
    for j in range(store_num):
        total += abs(store[i] - store[j])
    store[i] = total
    print(total)

min_value = min(store)
min_indices = [
    str(index + 1) for index, value in enumerate(store) if value == min_value
]
print(",".join(min_indices))
