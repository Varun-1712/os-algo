def exuction_of_FCFS(process):
    process.sort(key=lambda x: x["arrival_time"])
    time_count = process[i]["arrival_time"]

    process.sort(key=lambda x: x["burst_time"])

    i=0;
    count_of_i_for_condition_not_satisfy=0;
    complete_process=0

    while complete_process != process.length():
        if process[i]["remaining_burst_time"] == 0:
            continue;
        if time_count>=process[i]["arrival_time"]:
            process[i]["start_time"] = time_count
            time_count=time_count+ min(process[i]["remaining_burst_time"], process.quantum_time)
            process[i]["remaining_burst_time"]-=min(process[i]["remaining_burst_time"],process.quantum_time)
            if process[i]["remaining_burst_time"]==0:
                complete_process+=1
                count_of_i_for_condition_not_satisfy=0
                process[i]["end_time"]=time_count;
                process[i]["waiting_time"] = (
                process[i]["start_time"] - process[i]["arrival_time"]
                )
                process[i]["turnaround_time"] = (
                process[i]["end_time"] - process[i]["arrival_time"]
                )
        else:
            count_of_i_for_condition_not_satisfy+=1

        i+=1;
        i/=process.length()
        if(count_of_i_for_condition_not_satisfy==process.length()):
            process.sort(key=lambda x: x["arrival_time"])
            for i in range(0,process.length()):
                if process[i]["remaining_burst_time"] >0:
                    time_count = process[i]["arrival_time"]
            process.sort(key=lambda x: x["burst_time"]) 
            count_of_i_for_condition_not_satisfy=0       
    
            
    