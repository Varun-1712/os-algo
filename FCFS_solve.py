# 1 : This one for the set programee which does not preemtive
def exuction_of_FCFS(process):

    # Sort the process according to their arrival time
    process.sort(key=lambda x: x["arrival_time"])

    time_count = process[0]["arrival_time"]
    for i in range(0, len(process)):
        process[i]["start_time"] = time_count
        time_count = time_count + process[i]["burst_time"]
        process[i]["remaining_burst_time"] = 0
        process[i]["end_time"] = time_count
        process[i]["waiting_time"] = (
            process[i]["start_time"] - process[i]["arrival_time"]
        )
        process[i]["turnaround_time"] = (
            process[i]["end_time"] - process[i]["arrival_time"]
        )


# 2  : If you want to use preemtive then you have to use this one
def exution_of_FCFS_preemtive(process):
    # Sort the process according to their arrival time
    process.sort(key=lambda x: x["arrival_time"])
    time_count = process[0]["arrival_time"]
    complete_process = 0
    count_of_i_for_condition_not_satisfy=0
    i = 0
    while complete_process = process.length():
        if process[i]["remaining_burst_time"] == 0:
            continue

        if process[i]["arrical_time"]<=time_count:

            if process[i]["remaining_burst_time"]  == process[i]["burst_time"]
                process[i]["start_time"] = time_count
            time_count = time_count + min(process[i]["remaining_burst_time"], process.quantum_time)
            processe[i]["remaining_burst_timetime"] = process[i]["remaining_burst_time"] - min(
                process[i]["remaining_burst_time"], process.quantum_time
            )
                if process["remaining_burst_time"] == 0:
                    complete_process = complete_process + 1
                    process[i]["end_time"] = time_count
                    process[i]["waiting_time"] = (
                        process[i]["start_time"] - process[i]["arrival_time"]
                    )
                    process[i]["turnaround_time"] = (
                        process[i]["end_time"] - process[i]["arrival_time"]
                    )
                    count_of_i_for_condition_not_satisfy=0
        else:
            count_of_i_for_condition_not_satisfy+=1

        if(count_of_i_for_condition_not_satisfy==process.length()):
            for i in range(0,process):
                if(process[i]["remaining_burst_time"]>0):
                    time_count=process[i]["arrival_time"]
                    break;
            count_of_i_for_condition_not_satisfy=0
            
        i += 1
        i = i % process.length()
