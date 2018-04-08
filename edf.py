from utilityFunctions import *
from TaskItem import *

def deadline_run (sequence_time, TaskItem_list):
    time = 1
    print ("EDF scheduale \n")
    missed_deadline_counter = 0
    preemptive_counter = 0
    previous_task = TaskItem_list[0] #preemptive dummy value
    
    while time < sequence_time:
        has_run = False

        sorted_TaskItem_list = sorted(TaskItem_list, key=lambda TaskItem: TaskItem.deadline)
        #previous_task = sorted_TaskItem_list[0]

        #for loop to make it go through all the tasks :
        for curr_task_item in sorted_TaskItem_list:
            if(curr_task_item.done == False and has_run == False):
                curr_task_item.pr-=1
                #check preemptive after 2 seconds
                if (time > 1 and previous_task.id != curr_task_item.id and previous_task.done == False):
                    preemptive_counter +=1
                    print(" Task " + str(previous_task.id) + " is preemptive by Task " + str(curr_task_item.id))
                    previous_task.preemptedMissed +=1
                previous_task = curr_task_item
                if curr_task_item.pr == 0:
                    curr_task_item.done = True
                has_run = True         
            print(str(time).zfill(3) + " Task ID: "+ str(curr_task_item.id) +"  pr: " + str(curr_task_item.pr) +" ----- " + str(curr_task_item.done) +" ----- "+ " Deadline is: " + str(curr_task_item.deadline))
            if curr_task_item.deadline > time:
                pass
            else:
                if(not curr_task_item.done):
                    missed_deadline_counter+=1
                    curr_task_item.deadlineMissed +=1
                    missedDeadline(curr_task_item, time)

            if time % curr_task_item.period == 0: #if you're at the end of the period
                endOfPeriod (curr_task_item)

        time+=1
        print ("*********************")
    for deadlineEnd in sorted_TaskItem_list:
        if(deadlineEnd.done == False):
            missed_deadline_counter+=1
            deadlineEnd.deadlineMissed+=1
            print("Task " + str(deadlineEnd.id) + " missed the deadline at time " + str(time))
    print ("\n*********************")
    print("End of EDF \n" + "Number of preemptives: " + str(preemptive_counter) + "\nNumber of deadline misses: " + str(missed_deadline_counter))
    for output_task in sorted_TaskItem_list:
        print( "The task " + str(output_task.id) +" was preempted " + str(output_task.preemptedMissed) + " times and missed " + str(output_task.deadlineMissed) + " deadlines")
    #preemptions and deadline misses per task and in total.





