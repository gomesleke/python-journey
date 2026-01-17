import os
from function_json import open_json
from function_tasks import show_task

task_storage=open_json()

def clean_screen(): 
    os.system('cls')

def start():
    print('''
    | TAREFAS | 
        ''')
    print('Your Tasks: ')
    show_task(task_storage)



def main():
    start()
if __name__=='__main__':
    main()