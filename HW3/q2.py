work_seq_num = str(input())
work_hour = str(input())
work_ddl = str(input())

work_num, seq_num = [int(i) for i in work_seq_num.split(",")]
# Deal with input and make them lists
work_hour_list = [int(i) for i in work_hour.split(",")]
work_ddl_list = [int(i) for i in work_ddl.split(",")]

# load all possible sequences
work_seq_list = []
for i in range(seq_num):
    work_seq = str(input())
    work_seq_list.append([int(i) for i in work_seq.split(",")])


min_delay = 999999999
min_seq = 9999999999
cur_seq = 0
# Check for delayed work and time.
# 2-D array
for seq in work_seq_list:
    cur_seq += 1
    total_delay = 0
    time_now = 0
    for cur in seq:
        time_now += work_hour_list[cur - 1]
        delay = time_now - work_ddl_list[cur - 1]
        total_delay += delay if delay > 0 else 0
    if total_delay < min_delay:
        min_delay = total_delay
        min_seq = cur_seq

print(min_seq, ",", min_delay, sep="")
