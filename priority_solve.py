def exuction_of_Priority(process):

    sorted_process = sorted(process, key=lambda k: k["arrival_time"])
    time_count = sorted_process[0]["arrival_time"]
    sorted_process = sorted(process, key=lambda k: k['prority'])

    i=0
    count_of_i_for_condition_not_satisfy=0;
    while complete_process != process.length():
        if process[i]["arrical_time"]<=time_count:
            process[i]["start_time"] = time_count
            time_count=time_count+ process[i]["burst_time"]
            process[i]["remaining_burst_time"] = 0;
            process[i]["end_time"] = time_count;
            process[i]["waiting_time"] = process[i]["start_time"] - process[i]["arrival_time"]
            process[i]["turnaround_time"] = process[i]["end_time"] - process[i]["arrival_time"]
            count_of_i_for_condition_not_satisfy=0
            complete_process+=1
        else:
            count_of_i_for_condition_not_satisfy+=1
        i+=1
        i%=process.length()
        if(count_of_i_for_condition_not_satisfy==process.length()):
            process.sort(key=lambda x: x["arrival_time"])
            for i in range(0,process.length()):
                if process[i]["remaining_burst_time"] >0:
                    time_count = process[i]["arrival_time"]
            process.sort(key=lambda x: x["priority"]) 
            count_of_i_for_condition_not_satisfy=0
            
            
    