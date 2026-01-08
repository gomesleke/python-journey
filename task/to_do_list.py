import os

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

def choice():
    user_choice=int(input('Write your choice: '))

    try:
        match user_choice:
            case 1:
                print('vai corinthians')
            
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