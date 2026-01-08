import os

task_storage= []

def start():
    print('''\n| TO - DO LIST |''')
    print('\nthis is your to do list\n')

def menu():
    print('[1] - Add a Task')

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
            break

        task_sys={'status':check_task,'name':name_task_input}

        task_storage.append(task_sys)

        for task in task_storage:
            status_print='[X]' if task['status'] else '[ ]'
            print(f'{status_print} - {task['name']}')

        

def choice():
    user_choice=int(input('Write your choice: '))

    try:
        match user_choice:
            case 1:
                add_function()
            
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