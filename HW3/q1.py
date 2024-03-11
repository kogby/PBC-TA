work_num = int(input())
work_hour = str(input())
work_ddl = str(input())
work_seq = str(input())

# Deal with input and make them lists
work_hour_list = [int(i) for i in work_hour.split(",")]
work_ddl_list = [int(i) for i in work_ddl.split(",")]
work_seq_list = [int(i) for i in work_seq.split(",")]

total_delay = 0
time_now = 0
# Check for delayed work and time
for cur in work_seq_list:
    time_now += work_hour_list[cur - 1]
    delay = time_now - work_ddl_list[cur - 1]
    total_delay += delay if delay > 0 else 0

print(total_delay)
