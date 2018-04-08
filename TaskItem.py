class TaskItem(object):
    def __init__(self, task_string):
        task_list = task_string.split()
        task_list = list(map(int, task_list))
        self.id = task_list[0]
        self.done = False
        self.deadlineMissed = 0
        self.preemptedMissed = 0
        self.exn_time = task_list[1]
        self.period = task_list[2]
        self.deadline = task_list[3]
        self.pr = self.exn_time
        self.resource_id = None






