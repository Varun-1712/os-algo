class Scheduling_Algo:
    def __init__(self,n_process):
        processes = []
        for i in range(n_process):
            processes[i].arrival_time=0
            processes[i].burst_time=0
            processes[i].start_time=0
            processes[i].waiting_time=0
            processes[i].end_time=0
            processes[i].turnaround_time=0
        self.processes = processes

    def FCFS(self):
        pass
    
    def SJF(self):
        pass

    def RR(self):
        pass
    
    def SRTF(self):
        pass
    
    def PSJF(self):
        pass
    