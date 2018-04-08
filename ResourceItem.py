class ResourceItem(object):
    def __init__(self, resource_item_string):
        resource_list = resource_item_string.split()
        resource_list = list(map(int, resource_list))
        self.id = resource_list[0]
        self.number_of_tasks_that_use_this_resource = resource_list[1]
        self.tasks_that_use_this_resource = resource_list[2:]
        self.resource_in_use = False
