import json
import os

way='database/data.json'

def create_json(storage): #criar um json
    with open(way,'w') as file: #caminho
        json.dump(storage,file)

def open_json(): #abrir um json
    try:
        with open(way,'r') as file:
            data=json.load(file)
            return data
    
    except FileNotFoundError:
        print('Erro: Arquivo não encontrado')
        return None
    except json.JSONDecodeError:
        return None


def append_json(item): #adiciona no json
    storage = open_json()

    if not isinstance(storage, list): #isintance - O valor x é do tipo TIPO? ## se não houver lita, ele cria
        storage = []

    storage.append(item)
    create_json(storage)

def remove_json(item): #remove item
    storage = open_json()

    storage = [i for i in storage if i.get("task") != item]
    create_json(storage)

def clean_all(): #limpa tudo
    create_json([])



