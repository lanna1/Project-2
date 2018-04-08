from utilityFunctions import *
from TaskItem import *

def period_least_run (sequence_time, TaskItem_list, ResourceItem_resource_list):
    writingOutput = open("output1.txt", "a")
    #writingOutput.write("hello world suckas  " + str(random.randint(0, 10)) + "\n")

    time = 1
    writingOutput.write ("RM schedule \n")
    sorted_TaskItem_list = sorted(TaskItem_list, key=lambda TaskItem: TaskItem.period)
    sorted_ResourceItem_list = []

    # creating a sorted resource item list as determined by task item priority
    for t in sorted_TaskItem_list:
        for r in ResourceItem_resource_list:
            if t.resource_id == r.id and r not in sorted_ResourceItem_list:
                sorted_ResourceItem_list.append(r)


    previous_task = sorted_TaskItem_list[0] #preemptive

    missed_deadline_counter = 0
    preemptive_counter = 0

    while time < sequence_time:
        has_run = False

        #for loop to make it go through all the tasks
        for curr_task_item in sorted_TaskItem_list:
            if(curr_task_item.done == False and has_run == False):
                curr_task_item.pr-=1
                if (time > 1 and previous_task.id != curr_task_item.id and previous_task.done == False):
                    preemptive_counter+=1
                    writingOutput.write(" Task " + str(previous_task.id) + " is preemptive by Task " + str(curr_task_item.id) + "\n")
                    previous_task.preemptedMissed +=1
                previous_task = curr_task_item
                if curr_task_item.pr == 0:
                    curr_task_item.done = True
                has_run = True
            writingOutput.write(str(time).zfill(3) + " Task ID: "+ str(curr_task_item.id) +"  pr: " + str(curr_task_item.pr) +" ----- " + str(curr_task_item.done) + "\n")
            if curr_task_item.deadline > time:
                pass
            else:
                if(not curr_task_item.done):
                    missed_deadline_counter+=1
                    curr_task_item.deadlineMissed +=1
                    missedDeadline(curr_task_item, time)

            if time % curr_task_item.period == 0: #if you're at the end of the period
                endOfPeriod(curr_task_item)
        time+=1
        writingOutput.write ("*********************"+ "\n")
    for deadlineEnd in sorted_TaskItem_list:
        if(deadlineEnd.done == False):
            missed_deadline_counter+=1
            deadlineEnd.deadlineMissed+=1
            writingOutput.write("Task " + str(deadlineEnd.id) + " missed the deadline at time " + str(time)+ "\n")
    writingOutput.write ("*********************"+ "\n")
    writingOutput.write("End of RM \n" + "Number of preemptives: " + str(preemptive_counter) + "\nNumber of deadline misses: " + str(missed_deadline_counter)+ "\n")
    for output_task in sorted_TaskItem_list:
        writingOutput.write( "The task " + str(output_task.id) +" was preempted " + str(output_task.preemptedMissed) + " times and missed " + str(output_task.deadlineMissed) + " deadlines"+ "\n")

    writingOutput.close()