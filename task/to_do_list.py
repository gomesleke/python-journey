import os
import json #para armazenar os dados (estudar essa biblioteca)
import time

task_storage= []

if os.path.exists("task/database/tasks.json"): #para retomar
    with open("task/database/tasks.json", "r") as f:
        task_storage = json.load(f)

def start():
    print('''\n| TO - DO LIST |''')
    print('\nthis is your to do list\n')

def menu():
    print('[1] - Add a Task')
    print('[2] - Show HubTask')
    print('[3] - Completed Task')
    print('[4] - Exit')

def exit():
    clean_screen()
    print('Bye Bye...')
    time.sleep(0.5)
    print('I see you later')

def clean_screen():
    os.system('clear')

def invalid():
    clean_screen()
    print('You have a problem')
    input("Press to any keyboard: ")
    main()

def show_hub():
    for task in task_storage:
            status_print='[X]' if task['status'] else '[ ]'
            print(f'{status_print} - {task['name']}')

def save_json():
     with open("task/database/tasks.json", "w") as f:
            json.dump(task_storage, f)

def add_function():
    clean_screen()
    print('| MODE: ADD |')
    while True:

        
        name_task_input=input('Add your task (cls): ')
        check_task=False

        if name_task_input == 'cls':
            main()
            break
            

        task_sys={'status':check_task,'name':name_task_input}

        task_storage.append(task_sys)

        save_json()
        show_hub()


    

def choice():
    user_choice=int(input('Write your choice: '))

    try:
        match user_choice:
            case 1:
                add_function()

            case 2:
                show_hub()
            
            case 3:
                print('vai corinthians')

            case 4:
                exit()
            
            case _:
                invalid()
    except:
        invalid()

def main():
    clean_screen()
    start()
    menu()
    choice()

main()