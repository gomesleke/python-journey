import json
import os


def create_json(storage): #criar um json
    with open('data.json','w') as file:
        json.dump(storage,file)

def open_json(): #abrir um json
    try:
        with open('data.json','r') as file:
            data=json.load(file)
            return data
    
    except FileNotFoundError:
        print('Erro: Arquivo não encontrado')

        return None

