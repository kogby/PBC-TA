import copy

work_num = int(input())
work_hour = str(input())
work_ddl = str(input())
work_seq = str(input())

# Deal with input and make them lists
work_hour_list = [int(i) for i in work_hour.split(",")]
work_ddl_list = [int(i) for i in work_ddl.split(",")]
work_seq_list = [int(i) for i in work_seq.split(",")]


min_delay = 99999999

time_now = 0
# Check for delayed work and time
for i in range(work_num):
    total_delay = 0
    time_now = 0
    work_seq_list[i], work_seq_list[i - 1] = work_seq_list[i - 1], work_seq_list[i]
    for cur in work_seq_list:
        time_now += work_hour_list[cur - 1]
        delay = time_now - work_ddl_list[cur - 1]
        total_delay += delay if delay > 0 else 0
    min_delay = total_delay if min_delay > total_delay else min_delay

    work_seq_list[i - 1], work_seq_list[i] = work_seq_list[i], work_seq_list[i - 1]
print(min_delay)
