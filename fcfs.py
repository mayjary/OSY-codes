def fcfs(processes, burst_time):
    n = len(processes)
    waiting_time = [0] * n
    tat = [0] * n

    for i in range(1,n):
        waiting_time[i] = burst_time[i-1] + waiting_time[i-1]

    for i in range(n):
        tat[i] = burst_time[i] + waiting_time[i]

    avg_wt = sum(waiting_time)/n
    avg_tat = sum(tat)/n

    print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print("P"+str(processes[i])+"\t"+str(burst_time[i])+"\t"+str(waiting_time[i])+"\t"+str(tat[i]))

    print("Average Waiting time :", avg_wt)
    print("Average Turnaround time :", avg_tat)

n = int(input("Enter number of processes: "))
processes = [i+1 for i in range(n)]
burst_time = []
for i in range(n):
    bt = int(input("Enter Burst Time for Process " + str(i+1) + ": "))
    burst_time.append(bt)
fcfs(processes, burst_time)