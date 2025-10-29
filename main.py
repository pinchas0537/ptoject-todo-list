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
                print("זה עדיין בפיתוח")
            case "5":
                break
            case _:
                print("הבקשה לא נכונה!")
            
if __name__ == "__main__":            
    main()