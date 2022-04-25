# Import all required modules

from FCFS_solve import exuction_of_FCFS

# from SJF_solve import *
# from SRTF_solve import *
# from round_robin import *


class Scheduling_Algo:
    def __init__(self, n_process):
        process = []
        for i in range(0, n_process):
            process.append(
                {
                    "arrival_time": 0,
                    "burst_time": 0,
                    "remaining_burst_time": 0,
                    "start_time": 0,
                    "waiting_time": 0,
                    "end_time": 0,
                    "turnaround_time": 0,
                }
            )
        # print(process)
        self.processes = process
        self.quantum_time = 0
        self.preemtive_or_not = 1

    def add_process(self, process_id, arr_time, burst_time):
        self.processes[process_id-1]["arrival_time"] = arr_time
        self.processes[process_id-1]["burst_time"] = burst_time
        self.processes[process_id-1]["remaining_burst_time"] = burst_time

    def add_process(self, process_id, burst_time):
        self.processes[process_id-1]["burst_time"] = burst_time
        self.processes[process_id-1]["remaining_burst_time"] = burst_time

    def preemtive_or_not(self, yes_no):
        self.preemtive_or_not = yes_no

    def set_Quntem_time(self, quantum_time):
        self.quantum_time = quantum_time

    def FCFS(self):
        if(self.quantum_time==0):
            exuction_of_FCFS(self)
        else:
            exuction_of_FCFS_preemtive(self)



    def SJF(self):
        exuction_for_SJF(self)

    def SRTF(self):
        exuction_of_SRTF(self)
        

    # def RR(self):
    #     if self.preemtive_or_not == 0:
    #         print("You have to set preemtive to `1` to use RR")

    #     else:
    #         exuction_for_RR(self)
    #         pass

    #     pass


        



