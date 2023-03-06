import os
from platform import system as getos

from getkey import getkey



fileLocation = open('dir.txt').read()
if fileLocation == 'C:/Users/<user>/Documents/Github/Code/terminal':
    print("You need to set the file directory. Set it to the folder your 'terminal.py' file is in.\n\nExample (if your username was test):\nC:/Users/test/Documents/Github/Code/terminal\n")
else:

    backslash = '\\'

    # ANSI Color Codes
    codes = {
        'black_fore': '\033[30m',
        'red_fore': '\033[31m',
        'green_fore': '\033[32m',
        'yellow_fore': '\033[33m',
        'blue_fore': '\033[34m',
        'magenta_fore': '\033[35m',
        'cyan_fore': '\033[36m',
        'white_fore': '\033[37m',
        'bold': '\033[1m',
        'italic': '\033[3m',
        'underline': '\033[4m',
        'strikethrough': '\033[9m',
        'reset': '\033[0m'
    }

    # Console Commands
    commands = {
        'mkdir': '''try: 
    os.mkdir(cmd[6:])
except:
    print(f"Error: Directory \'{cmd[6:]}\' already exists.")''',
        
        'rmdir': '''for i in cmd[6:].split(" "):
    os.system(f"rmdir /s {i}")''',
        
        'mkfile': '''try:
    open(cmd[7:], "x")
except:
    print(f"Error: File \'{cmd[7:]}\' already exists.")''',
        
        'rmfile': '''if getos() == "Windows":
    for i in cmd[7:].split(" "):
        os.system(f"del {i}")
elif getos() == "Linux":
    for i in cmd[7:].split(" "):
        os.system(f"rm {i}")''',
        
        'cd': '''try:
    if cmd.strip() == "cd":
        os.chdir(filelocation + f"/data/{user}")
    else:
        os.chdir(cmd[3:])
except:
    print(f"Error: Directory \'{cmd[3:]}\' does not exist.")''',
    
        'writetofile': '''with open(cmd[12:], "w") as file:
    final = ""
    print()
    while getkey() != "`":
        final += getkey()
    file.write(final)''',
        
        'ls': '''for i in os.listdir():
    print(i)''',
        
        'read': '''try:
    print(open(cmd[5:]).read())
except:
    print(f"Error: File \'{cmd[5:]}\' does not exist.")''',
        
        'deluser': '''if cmd.strip() == "deluser":
    username = input("Username: ")
else:
    username = cmd[8:]
userpassword = input("Password: ")
if check_login(username, userpassword) == 0:
    os.system(f"rmdir /s {username})
    print(f"User \'{username}\' deleted.")
elif check_login(username, userpassword) == 1:
    print("The username or password is incorrect.")
else:
    print("That user doesn't exist.")
        ''',
    
        'clear': '''if getos() == "Windows":
    os.system("cls")
else:
    os.system("clear")''',
    
        'stop': '''quit()'''
    }



    loggedInUser = ''

    usersList = open("users.txt").read()


    def reset():
        os.system('rmdir /s data')
        os.mkdir('data')
        with open("users.txt", 'w') as users:
            users.write('')

        
    def create_account(username, password):
        if f'{username} {password}' not in open(fileLocation + "/users.txt").read():
            open(fileLocation + "/users.txt", 'a').write(f'{username} {password}\n')
            os.chdir(fileLocation + '/data')
            try:
                os.mkdir(username)
            except:
                print()
            os.chdir('..')
        else:
            print("That account already exists.")
        

    def create_account_screen():
        print(f"{codes['bold']}\nCreate Account Screen{codes['reset']}")
        username = input("Username for New Account: ")
        password = input("Password for New Account: ")
        create_account(username, password)
        print("You created a new account!")
        login_screen()
        
        
    def login(username, password):
        if username + " " in open("users.txt").read().strip():
            usernamePos = open("users.txt").read().strip().index(username)
            if open("users.txt").read().strip()[usernamePos+len(username)+1:open("users.txt").read().strip().find("\n", usernamePos+len(username))] == password:
                runterminal(username)
                return 0
            else:
                return 1
        else:
            return 2
        
        
    def login_screen():
        if open("users.txt").read().strip() == '':
            print("You don't have any users, so you are being directed to the account creation screen. (After creating account, you have to restart the program for it to )")
            create_account_screen()
        else:
            print("\nLog in to a user: ")
            username = input("Username: ")
            password = input("Password: ")
            if login(username, password) == 0:
                print(f"You are successfully logged in to the '{username}' account!")
                runterminal(username)
            elif login(username, password) == 1:
                print("\nEither The username or password you inputed is incorrect.")
                login_screen()
            else:
                print(f"The user '{username}' does not exist! Do you want to create an account? (Y/n): ")
                while getkey().lower() != 'y' or getkey().lower() != 'n':
                    if getkey().lower() == 'y':
                        create_account_screen()
                    elif getkey().lower() == 'n':
                        login_screen()


    def runterminal(user):
        startdir = os.getcwd().replace(backslash, "/").replace(user, '~', 1).split("/")
        cmd = ''
        os.chdir(fileLocation + f'/data/{user}')
        while cmd != 'logout': 
            dir = (os.getcwd().replace(backslash, "/").replace(user, '~', 1).split("/"))[len(startdir):]
            usingdir = ""
            for i in dir:
                usingdir += i + '/'
            usingdir = usingdir.replace('data/', '')
            cmd = input(codes['blue_fore'] + f'{user}: {usingdir}{codes["reset"]}$ ')
            for i in commands:
                if cmd.startswith(i):
                    exec(commands[i])
        login_screen()


    login_screen()