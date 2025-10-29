import game

def main() -> None:
    while True:
        show = game.get_user_choice()
        match show:
            case "1":
                task = input("Enter a task:")
                game.add_task(game.todo_list,task)
            case "2":
                game.show_all_tasks(game.todo_list)
            case "3":
                game.show_all_tasks(game.todo_list)
                index = int(input("Which task to delete? (Choose a number)"))
                game.delete_task(game.todo_list,index)
            case "4":
                if len(game.todo_list) > 0:
                    game.show_all_tasks(game.todo_list)
                    index = int(input("Which task to edit? (Choose a number)"))
                    nwo_task = input("Please enter the new task:")
                    game.edit_task(game.todo_list,index,nwo_task)
                else:
                    print ("The list is empty.")
            case "5":
                index = int(input("Enter the task number you want to see."))
                game.get_task_index_from_user(index)
            case "6":
                if len(game.todo_list) > 0:
                    keyword = input("Enter a word you want to search for:")
                    game.search_tasks(game.todo_list,keyword)
                else:
                    print ("The list is empty.")
            case "7":
                break
            case _:
                print("הבקשה לא נכונה!")
            
if __name__ == "__main__":            
    main()