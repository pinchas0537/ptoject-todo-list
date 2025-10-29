todo_list = []

def add_task(tasks: list, task: str) -> None:
    tasks.append(task)
    pass

def show_all_tasks(tasks: list) -> None:
    if len(tasks) == 0:
        print("The list is empty!")
    else:
        index = 0
        for task in tasks:
            index +=1
            print(f"{index}. {task}" )