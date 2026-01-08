import os
import json #para armazenar os dados (estudar essa biblioteca)

task_storage= []

if os.path.exists("tasks.json"): #para retomar
    with open("tasks.json", "r") as f:
        task_storage = json.load(f)

def start():
    print('''\n| TO - DO LIST |''')
    print('\nthis is your to do list\n')

def menu():
    print('[1] - Add a Task')
    print('[2] - Show HubTask')

def clean_screen():
    os.system('cls')

def invalid():
    clean_screen()
    print('You have a problem')
    input("Press to any keyboard: ")
    main()

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

        with open("tasks.json", "w") as f:
            json.dump(task_storage, f)


        for task in task_storage:
            status_print='[X]' if task['status'] else '[ ]'
            print(f'{status_print} - {task['name']}')

def choice():
    user_choice=int(input('Write your choice: '))

    try:
        match user_choice:
            case 1:
                add_function()

            case 2:
                print(task_storage)
            
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