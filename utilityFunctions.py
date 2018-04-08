from TaskItem import *


def missedDeadline(curr_task_item, time):
    print(str(time).zfill(3) + " TASK  " + str(curr_task_item.id) + " DEADLINE MISSED")
    curr_task_item.done = True #to make sure it doesn't run when it missed deadline

def endOfPeriod (curr_task_item):
    curr_task_item.pr = curr_task_item.exn_time
    curr_task_item.done = False
    curr_task_item.deadline+=curr_task_item.period

