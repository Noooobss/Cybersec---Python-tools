##!/usr/bin/env python3

##   CYBERSEC 	    : 	CyberSecurity Launcher, Resources & Tools
##   Author      	: 	Noooob
##   Version     	: 	1.0
##   Github      	: 	https://github.com/Noooobss
##   Inspiration    :   Copyright (c) 2022 C.RANJITH KUMAR

import sys
import time
from colorama import init, Fore
import inquirer
import os
import getpass
from rich.console import Console
from rich.spinner import Spinner
import pymongo
from hashlib import sha256
import re
from platform import system

init()
colors = {
    "red": Fore.RED,
    "green": Fore.GREEN,
    "blue": Fore.BLUE,
    "yellow": Fore.YELLOW,
    "purple": Fore.MAGENTA,
    "reset": Fore.RESET,
    "cyan": Fore.CYAN
}




class Main():
    def __init__(self):
        self.Clear()
        self.cluster = pymongo.MongoClient("mongodb+srv://projetosjosesdoudos:l33ArNvSxwRzNf6D@database.ubnz9y7.mongodb.net/?retryWrites=true&w=majority&appName=DataBase")
        self.db = self.cluster.get_database("Logins")
        self.collection = self.db.get_collection("Users/Passwords/Keys")
    def Clear(self):
        if (os.name == "posix"):
            os.system("clear")
        elif (os.name == "nt"):
            os.system("cls")
        else:
            pass

    def Menu(self):
        self.Clear()
        print(rf"""{colors["green"]}
        

                         .-. .-')      ('-.    _  .-')     .-')       ('-.                  .-') _                                           .-')    
                         \  ( OO )   _(  OO)  ( \( -O )   ( OO ).   _(  OO)                (  OO) )                                         ( OO ).  
   .-----.    ,--.   ,--. ;-----.\  (,------.  ,------.  (_)---\_) (,------.    .-----.    /     '._   .-'),-----.  .-'),-----.  ,--.      (_)---\_) 
  '  .--./     \  `.'  /  | .-.  |   |  .---'  |   /`. ' /    _ |   |  .---'   '  .--./    |'--...__) ( OO'  .-.  '( OO'  .-.  ' |  |.-')  /    _ |  
  |  |('-.   .-')     /   | '-' /_)  |  |      |  /  | | \  :` `.   |  |       |  |('-.    '--.  .--' /   |  | |  |/   |  | |  | |  | OO ) \  :` `.  
 /_) |OO  ) (OO  \   /    | .-. `.  (|  '--.   |  |_.' |  '..`''.) (|  '--.   /_) |OO  )      |  |    \_) |  |\|  |\_) |  |\|  | |  |`-' |  '..`''.) 
 ||  |`-'|   |   /  /\_   | |  \  |  |  .--'   |  .  '.' .-._)   \  |  .--'   ||  |`-'|       |  |      \ |  | |  |  \ |  | |  |(|  '---.' .-._)   \ 
(_'  '--'\   `-./  /.__)  | '--'  /  |  `---.  |  |\  \  \       /  |  `---. (_'  '--'\       |  |       `'  '-'  '   `'  '-'  ' |      |  \       / 
   `-----'     `--'       `------'   `------'  `--' '--'  `-----'   `------'    `-----'       `--'         `-----'      `-----'  `------'   `-----'  

{colors["reset"]}
""")
        self.options = [
            inquirer.List("choice",
                          message = f"Welcome, please choose one of the options below",
                          choices = [
                              " Login",
                              " Register",
                              " Exit",
                              ],
                          ),
            ]
        self.choice = inquirer.prompt(self.options)
        if (self.choice["choice"] == " Login"):
            self.Login()
        elif (self.choice["choice"] == " Register"):
            self.Register()
        elif (self.choice["choice"] == " Exit"):
            self.Exit()
        else:
            pass

    def Confirm_continue(self):
        self.Clear()
        self.options_continue = [
            inquirer.List("choice_continue",
                          message = f"Would you like to continue?",
                          choices = [
                              " Continue",
                              " Return",
                              ],
                          ),
            ]
        self.choice_continue = inquirer.prompt(self.options_continue)
        if (self.choice_continue["choice_continue"] == " Continue"):
            pass
        elif (self.choice_continue["choice_continue"] == " Return"):
            self.Menu()

    def Tools(self):
        self.Clear()
        print(f"""{colors["cyan"]}
                ⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠟⠃⠀⠀⠙⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠋⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠾⢛⠒⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣶⣄⡈⠓⢄⠠⡀⠀⠀⠀⣄⣷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣷⠀⠈⠱⡄⠑⣌⠆⠀⠀⡜⢻⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡿⠳⡆⠐⢿⣆⠈⢿⠀⠀⡇⠘⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣷⡇⠀⠀⠈⢆⠈⠆⢸⠀⠀⢣⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣧⠀⠀⠈⢂⠀⡇⠀⠀⢨⠓⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣦⣤⠖⡏⡸⠀⣀⡴⠋⠀⠈⠢⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠁⣹⣿⣿⣿⣷⣾⠽⠖⠊⢹⣀⠄⠀⠀⠀⠈⢣⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⣇⣰⢫⢻⢉⠉⠀⣿⡆⠀⠀⡸⡏⠀⠀⠀⠀⠀⠀⢇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⡇⡇⠈⢸⢸⢸⠀⠀⡇⡇⠀⠀⠁⠻⡄⡠⠂⠀⠀⠀⠘
⢤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠛⠓⡇⠀⠸⡆⢸⠀⢠⣿⠀⠀⠀⠀⣰⣿⣵⡆⠀⠀⠀⠀
⠈⢻⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⣦⣀⡇⠀⢧⡇⠀⠀⢺⡟⠀⠀⠀⢰⠉⣰⠟⠊⣠⠂⠀⡸
⠀⠀⢻⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢧⡙⠺⠿⡇⠀⠘⠇⠀⠀⢸⣧⠀⠀⢠⠃⣾⣌⠉⠩⠭⠍⣉⡇
⠀⠀⠀⠻⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣞⣋⠀⠈⠀⡳⣧⠀⠀⠀⠀⠀⢸⡏⠀⠀⡞⢰⠉⠉⠉⠉⠉⠓⢻⠃
⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⢀⣀⠠⠤⣤⣤⠤⠞⠓⢠⠈⡆⠀⢣⣸⣾⠆⠀⠀⠀⠀⠀⢀⣀⡼⠁⡿⠈⣉⣉⣒⡒⠢⡼⠀
⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣎⣽⣶⣤⡶⢋⣤⠃⣠⡦⢀⡼⢦⣾⡤⠚⣟⣁⣀⣀⣀⣀⠀⣀⣈⣀⣠⣾⣅⠀⠑⠂⠤⠌⣩⡇⠀
⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⣺⢁⣞⣉⡴⠟⡀⠀⠀⠀⠁⠸⡅⠀⠈⢷⠈⠏⠙⠀⢹⡛⠀⢉⠀⠀⠀⣀⣀⣼⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⡟⢡⠖⣡⡴⠂⣀⣀⣀⣰⣁⣀⣀⣸⠀⠀⠀⠀⠈⠁⠀⠀⠈⠀⣠⠜⠋⣠⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⡟⢿⣿⣿⣷⡟⢋⣥⣖⣉⠀⠈⢁⡀⠤⠚⠿⣷⡦⢀⣠⣀⠢⣄⣀⡠⠔⠋⠁⠀⣼⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡄⠈⠻⣿⣿⢿⣛⣩⠤⠒⠉⠁⠀⠀⠀⠀⠀⠉⠒⢤⡀⠉⠁⠀⠀⠀⠀⠀⢀⡿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣤⣤⠴⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠤⠀⠀⠀⠀⠀⢩⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                          {colors["reset"]}{colors["red"]}CodingNoooob{colors["reset"]}                 
                \033[32m[@] Set Path (All your tools will be installed in that directory)
              \033[37m[X]All In One Tools For Cybersecurity Updated by Coding Noooob
        \033[35m [✔] 𝗩𝗲𝗿𝘀𝗶𝗼𝗻 𝟮.𝟬 [✔]\033[32m[✔]- 𝗕𝗲𝗴𝗶𝗻𝗻𝗲𝗿 𝗙𝗿𝗶𝗲𝗻𝗱𝗹𝘆 -[✔]
           \033[91m[!] 𝗣𝗹𝗲𝗮𝘀𝗲 𝗗𝗼𝗻❜𝘁 𝗨𝘀𝗲 𝗙𝗼𝗿 𝗶𝗹𝗹𝗲𝗴𝗮𝗹 𝗔𝗰𝘁𝗶𝘃𝗶𝘁𝘆  [!]""")
        self.tool = [
            inquirer.List("tool",
                          message = f" Set Path (All your tools will be installed in that directory)",
                          choices = [
                              " Manual",
                              " Default",
                              ],
                          ),
            ]
        self.choice_tool = inquirer.prompt(self.tool)
        if (self.choice_tool["tool"] == " Manual"):
            self.inpatch = input("Enter Path (with Directory Name) >> ")
            if (system() == 'Linux'):
                self.fpathlinux = "/home/cybersec.txt"
                with open(self.fpathlinux, "w") as f:
                    f.write(self.inpath)
                    print(f"Successfully Set Path to: {self.inpath}")
        elif (self.choice_tool["tool"] == " Default"):
            if (system() == 'Linux'):
                self.autopathlinux = "/home/Cybersec---Python-tools/"
                with open(self.autopathlinux, "w") as f:
                    f.write(self.autopathlinux)
                    print(f"Your Default Path Is: {self.autopathlinux}")
            
        else:
            pass
    def Exit(self):
        for cont in range (3, 0, -1):
            sys.stdout.write(f"[{colors['red']}-{colors['red']}] Leaving in {cont}")
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write("\r" + " " * 120 + "\r")
        sys.stdout.flush()
        sys.exit(0)
    def EnterSomething(self):
        for cont in range(3, 0, -1):
            sys.stdout.write(f"[{colors['red']}-{colors['red']}] Invalid, please enter something {cont}")
            sys.stdout.flush()
            time.sleep(1)
        #sys.stdout.write("\r" + " " * 100 + "\r")
        #sys.stdout.flush() 
        self.Login()
    def Login(self):
        self.Confirm_continue()
        self.Clear()
        print(rf"""{colors["green"]}


                                                    .-') _  
                                                   ( OO ) ) 
 ,--.       .-'),-----.   ,----.       ,-.-')  ,--./ ,--,'  
 |  |.-')  ( OO'  .-.  ' '  .-./-')    |  |OO) |   \ |  |\  
 |  | OO ) /   |  | |  | |  |_( O- )   |  |  \ |    \|  | ) 
 |  |`-' | \_) |  |\|  | |  | .--, \   |  |(_/ |  .     |/  
(|  '---.'   \ |  | |  |(|  | '. (_/  ,|  |_.' |  |\    |   
 |      |     `'  '-'  ' |  '--'  |  (_|  |    |  | \   |   
 `------'       `-----'   `------'     `--'    `--'  `--'   

{colors["reset"]}
""")
        print(f"[{colors['yellow']}?{colors['reset']}] Log in:")
        self.username = input(f"[{colors['green']}+{colors['reset']}] CodingNoooob =>> Username: ")
        if (not self.username):
            self.EnterSomething()
        else:
            pass
        self.password = getpass.getpass(f"[{colors['green']}+{colors['reset']}] CodingNoooob =>> Password: ")
        if (not self.password):
            self.EnterSomething()
        else:
            pass
        console = Console()
        with console.status("Checking in data base", spinner = "moon"):
            self.user = self.collection.find_one({"User": self.username})
            time.sleep(3)
        if (self.user and self.user["Password"] == self.password):
            for cont in range (3, 0, -1):
                sys.stdout.write(f"\r[{colors['yellow']}+{colors['reset']}] Login successful. Redirecting in {cont}")
                sys.stdout.flush()
                time.sleep(1)
                
            sys.stdout.write("\r" + " " * 120 + "\r")
            sys.stdout.flush()
            #implement system redirection 
            self.Tools()
        else:
            self.RetryLogin()
    def RetryLogin(self):
        for cont in range (3, 0, -1):
            sys.stdout.write(f"\r[{colors['red']}-{colors['reset']}] User or password incorrect {cont}")
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write("\r" + " " * 120 + "\r")
        sys.stdout.flush()
        self.Login()
    def Register(self):
        self.Confirm_continue()
        self.Clear()
        print(rf"""{colors["green"]}


 _  .-')      ('-.                            .-')     .-') _       ('-.    _  .-')   
( \( -O )   _(  OO)                          ( OO ).  (  OO) )    _(  OO)  ( \( -O )  
 ,------.  (,------.   ,----.       ,-.-')  (_)---\_) /     '._  (,------.  ,------.  
 |   /`. '  |  .---'  '  .-./-')    |  |OO) /    _ |  |'--...__)  |  .---'  |   /`. ' 
 |  /  | |  |  |      |  |_( O- )   |  |  \ \  :` `.  '--.  .--'  |  |      |  /  | | 
 |  |_.' | (|  '--.   |  | .--, \   |  |(_/  '..`''.)    |  |    (|  '--.   |  |_.' | 
 |  .  '.'  |  .--'  (|  | '. (_/  ,|  |_.' .-._)   \    |  |     |  .--'   |  .  '.' 
 |  |\  \   |  `---.  |  '--'  |  (_|  |    \       /    |  |     |  `---.  |  |\  \  
 `--' '--'  `------'   `------'     `--'     `-----'     `--'     `------'  `--' '--' 

{colors["reset"]}
""")
        print(f"[{colors['yellow']}?{colors['reset']}] Register:")
        self.username_register = input(f"[{colors['green']}+{colors['reset']}] CodingNoooob =>> Username: ")
        if (not self.username_register):
            self.EnterSomething()
        self.password_register = getpass.getpass(f"[{colors['green']}+{colors['reset']}] CodingNoooob =>> Password: ")
        if (not self.password_register):
            self.EnterSomething()
        self.key_register = input(f"[{colors['green']}+{colors['reset']}] Key: ")
        if (not self.key_register):
            self.EnterSomething()
        if (self.collection.find_one({"User": self.username_register})):
            self.RetryRegister()
        self.collection.insert_one({
            "User": self.username_register,
            "Password": self.password_register,
            "Key": self.key_register
        })
        for cont in range (3, 0, -1):
                sys.stdout.write(f"\r[{colors['yellow']}+{colors['reset']}] Successfully added. Redirecting in {cont}")
                sys.stdout.flush()
                time.sleep(1)
    def RetryRegister(self):
        for cont in range (3, 0, -1):
            sys.stdout.write(f"\r[{colors['red']}-{colors['reset']}] Error, existing user {cont}")
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write("\r" + " " * 120 + "\r")
        sys.stdout.flush()
        self.Register()
if (__name__ == "__main__"):
    Main = Main()
    Main.Menu()