import os
import json
from function_json import append_json
from function_json import remove_json
from function_json import open_json
from function_json import clean_all

task_storage=open_json()

def add_task(): 

    while True: 
        task=input('Your Tasks("cls" to finish): ')
        if task=='cls':
            break
        
        task_dic={
            'task':task,
            'check':False
        }
        append_json(task_dic)

def rm_task(): 
    while True:
        task=input('Remove Tasks("cls" to finish): ')
        if task=='cls':
            break
        remove_json(task)

def show_task(data):
    for task in data:
            status_print='[X]' if task['check'] else '[ ]'
            print(f'{status_print} - {task['task']}')


