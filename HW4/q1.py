job_cnt = int(input())
processing_times = str(input())
due_times = str(input())
init_seq = str(input())

# Deal with input and make them lists
processing_times_list = [int(i) for i in processing_times.split(",")]
due_times_list = [int(i) for i in due_times.split(",")]
init_seq_list = [int(i) for i in init_seq.split(",")]


# ==================================================== Above is provided

# Initialize the minimum to find
best_found = True
best_work_seq = init_seq_list
min_delay = 99999999
while best_found:
    # Initialize loop condition to false
    best_found = False

    # Generate all possible sequences
    possible_seq = [best_work_seq]
    for i in range(job_cnt):
        tmp_list = [j for j in best_work_seq]
        if i == job_cnt - 1:
            tmp_list[i], tmp_list[0] = tmp_list[0], tmp_list[i]
        else:
            tmp_list[i], tmp_list[i + 1] = tmp_list[i + 1], tmp_list[i]
        possible_seq.append(tmp_list)

    # Calculate delay time for each sequence
    for seq in possible_seq:
        # print("Current Work flow:",seq)
        total_delay = 0
        time_now = 0
        for cur in seq:
            time_now += processing_times_list[cur - 1]
            delay = time_now - due_times_list[cur - 1]
            total_delay += delay if delay > 0 else 0
        if min_delay > total_delay:
            min_delay = total_delay
            best_work_seq = seq
            best_found = True

# Print the best sequence and the minimum delay
print(f"{','.join(map(str, best_work_seq))};{min_delay}")
