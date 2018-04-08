from TaskItem import TaskItem
from RM import *
from edf import *
import copy

from ResourceItem import ResourceItem

def main():
    ################ PARSING TASK LIST ################
    # import input file into a list of task strings
    with open("Test1.txt") as f:
        content = f.readlines()
        content = [x.strip() for x in content]

    # take the first and last lines and assign appropriate vals
    number_of_tasks = int(content[0])
    sequence_time = int(content[-1][2:]) #200

    # remove first and last lines, leaving only task
    content.pop(0)
    content.pop(-1)

    raw_task_list = content
    TaskItem_list = []

    for raw_task in raw_task_list[:number_of_tasks]:
        TaskItem_list.append(TaskItem(raw_task))

    ################ PARSING RESOURCE LIST ############

    # import resource file into list of resource strings
    with open("ResourceFile.txt") as f2:
        resourceContent = f2.readlines();
        resourceContent = [x.strip() for x in resourceContent]

    # take the first line and assign appropriate val
    number_of_tasks_in_resource_file = int(resourceContent[0])
    if(number_of_tasks != number_of_tasks_in_resource_file):
        print("Mismatch between resource file task number and task file task number")
        exit(0)
    number_of_resources = int(resourceContent[1])

    resourceContent.pop(0)
    resourceContent.pop(0)

    print(resourceContent)

    raw_resource_list = resourceContent
    ResourceItem_list = []

    for raw_resource in raw_resource_list:
        ResourceItem_list.append(ResourceItem(raw_resource))

    #Setting each TaskItem's resourceId
    for t in TaskItem_list:
        for r in ResourceItem_list:
            if t.id in r.tasks_that_use_this_resource:
                t.resource_id = r.id



    ###################################################

    for num, item in enumerate(TaskItem_list):
        print("Periodic Index of {} id of {} and execuation time of  {} " .format(num, item.id, item.exn_time))


   # i is the index
   # item is your item in enum1
    rm_task_list = copy.deepcopy(TaskItem_list)
    rm_resource_list = copy.deepcopy(ResourceItem_list)

    # edf_list = copy.deepcopy(TaskItem_list)
    #runs the RM file
    period_least_run (sequence_time, rm_task_list, rm_resource_list)
    #runs the EDF file
    # deadline_run (sequence_time, edf_list)
    #runs RM with aperiodic tasks
    #rm_with_aperiodic (sequence_time, TaskItem_list, aperiodic_list, number_of_aperiodic,deferrable_server )


main()


#store of the previous task and check when in the if statement if has run
#if it isn't the same as previous task and it wasn't done then it is premepted
#Label <space> arrival time <space> execution time










