import os
from function_json import open_json
from function_task import show_task
from function_task import add_task
from function_task import rm_task

task_storage=open_json()

def clean_screen(): 
    os.system('cls')

def start():
    print('''
    | TAREFAS | 
        ''')
    print('Your Tasks: ')
    
    print('\n\n')
    
    print('[1] - Add a Task')
    print('[2] - Show HubTask')
    print('[3] - Completed Task')
    print('[4] - Sair')

def invalid():
    clean_screen()
    print('You have a problem')
    input("Press to any keyboard: ")
    main()

def choice_menu():
    choice=int(input(' Escolha uma opção'))
    
    try:
        match choice:
            case 1:
                add_task()

            case 2:
                show_task(task_storage)
            
            case 3:
                print('vai corinthians')

            case 4:
                exit()
            
            case _:
                invalid()
    except:
        invalid()
        

def main():
    start()
if __name__=='__main__':
    main()