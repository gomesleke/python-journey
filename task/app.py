import os
import json
from function_json import append_json
from function_json import remove_json

def add_task(task): 

    while True: 
        task=input('Your Tasks("cls" to finish): ')
        if task=='cls':
            break
        else:
            append_json(task)

def rm_task(task): 
    while True:
        task=input('Remove Tasks("cls" to finish): ')
        if task=='cls':
            break
        else:
            remove_json(task)



