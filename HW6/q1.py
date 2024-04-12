file_path = input()
log_num = int(input())
analysis_mode = str(input())


def custom_sort(item):
    return (-item[1], len(item[0]), item[0])


def analysis_by_sid(log_lists: list):
    total_by_sid = {}
    for sid, date, pid, quantity, price in log_lists:
        quantity = int(quantity)
        price = int(price)
        if sid in total_by_sid:
            total_by_sid[sid] += quantity * price
        else:
            total_by_sid[sid] = quantity * price
    sorted_total = sorted(total_by_sid.items(), key=custom_sort)
    return sorted_total


def analysis_by_pid(log_lists: list):
    total_by_pid = {}
    for sid, date, pid, quantity, price in log_lists:
        quantity = int(quantity)
        price = int(price)
        if pid in total_by_pid:
            total_by_pid[pid] += 1
        else:
            total_by_pid[pid] = 1
    sorted_total = sorted(total_by_pid.items(), key=custom_sort)
    return sorted_total


log_lists = []
with open(file_path, "r") as file:
    line = file.readline()
    for _ in range(log_num):
        line = file.readline()
        log_lists.append([i for i in line.strip().split(",")])
total = (
    analysis_by_sid(log_lists) if analysis_mode == "S" else analysis_by_pid(log_lists)
)
for i in total[:3]:
    print(f"{i[0]},{i[1]}")
