def find_store_or_product(id, store_rev: dict, product_sales_cnt: dict):
    if id in store_rev.keys():
        return store_rev[id]
    elif id.isdigit() and int(id) in product_sales_cnt.keys():
        return product_sales_cnt[int(id)]
    else:
        raise KeyError


file_name = input().strip()
store_rev = {}
product_sales_cnt = {}

with open(file_name, "r", newline="") as txtfile:
    next(txtfile)
    for line in txtfile:
        row = line.strip().split(",")
        sid, pid, qty, unit_price = row[0], int(row[2]), int(row[3]), int(row[4])
        revenue = qty * unit_price

        if sid not in store_rev:
            store_rev[sid] = 0
        store_rev[sid] += revenue

        if pid not in product_sales_cnt:
            product_sales_cnt[pid] = 0
        product_sales_cnt[pid] += 1

data_count, query_len = map(int, input().split(","))
queries = []
for i in range(query_len):
    query = input().strip()
    queries.append(query)

for query in queries:
    try:
        result = find_store_or_product(query, store_rev, product_sales_cnt)
        print(result)
    except KeyError:
        print("BAD!!")
