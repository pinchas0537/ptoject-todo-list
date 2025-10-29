todo_list = []

def add_task(tasks: list, task: str) -> None:
    tasks.append(task)
 
def show_all_tasks(tasks: list) -> None:
    if len(tasks) == 0:
        print("The list is empty!")
    else:
        index = 0
        for task in tasks:
            index +=1
            print(f"{index}. {task}" )

def get_user_choice() -> str:
    choice  = input("""
        1. הוספת משימה
        2. הצגת כל המשימות
        3. מחיקת משימה
        4. עריכת משימה
        5. הצגת מיקום משימה ברשימה
        6. יציאה
        בחר את האפשרות הרצויה: """)
    return choice

def delete_task(tasks: list, index: int) -> bool:
    if index <= len(tasks):
        tasks.pop(index - 1)
        print("The task was successfully deleted!")
        return True
    else:
        print("No such number was found in the list!")
        return  False
    
def edit_task(tasks: list, index: int, new_task: str) -> bool:
    if index <= len(tasks):
        tasks[index -1] = new_task
        print("The task has been updated successfully!")
        return True
    else:
        print("No such number was found in the list!")
        return  False

def get_task_index_from_user(index: int) -> int:
    if index > 0:
        print(f"The mission index is: {index - 1}")
    else:
        print("Invalid input")