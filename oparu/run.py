from bullet import Bullet, Check, YesNo, Input, Password, SlidePrompt, VerticalPrompt, colors
from bullet.utils import clearConsoleUp, clearLine
from validate_user import is_users, add_user
from colorama import Fore
import time 

def start_cli():
    print("""
    
 ▄██████▄     ▄███████▄    ▄████████    ▄████████ ███    █▄  
███    ███   ███    ███   ███    ███   ███    ███ ███    ███ 
███    ███   ███    ███   ███    ███   ███    ███ ███    ███ 
███    ███   ███    ███   ███    ███  ▄███▄▄▄▄██▀ ███    ███ 
███    ███ ▀█████████▀  ▀███████████ ▀▀███▀▀▀▀▀   ███    ███ 
███    ███   ███          ███    ███ ▀███████████ ███    ███ 
███    ███   ███          ███    ███   ███    ███ ███    ███ 
 ▀██████▀   ▄████▀        ███    █▀    ███    ███ ████████▀  
                                       ███    ███ """)
                                       
    print(Fore.WHITE + "      version: " + Fore.MAGENTA + "0.0.1")
    print(Fore.WHITE + "      author: " + Fore.MAGENTA + "@ligula" + Fore.WHITE)
    menu_start()

def menu_start():
    #UI Colour assignment 
    bright_cyan = colors.bright(colors.foreground["cyan"])

    choices = is_users()
    menu = SlidePrompt(
        [
            Bullet("\nOparu v0.0.1", 
                choices = choices,
                bullet="",
                indent = 0,
                pad_right = 8, 
                shift = 1, 
                align = 1, 
                margin = 2)
        ]
    )

    result = menu.launch()
    if result[0][1] == "Continue":
        continue_user()
    else:
        new_user()
 

def continue_user():
    user_input = VerticalPrompt(
        [
            Input("username: ", indent = 0),
            Password("password: ", hidden = "*", indent = 0),
        ],
        spacing = 0     
    )
    user_login = user_input.launch()
    print(user_login[0][1])


def new_user():
    user_input = VerticalPrompt(
        [
            Input("username: ", indent = 0),
            Password("password: ", hidden = "*", indent = 0),
            Password("repeat password: ", hidden = "*", indent = 0),
        ],
        spacing = 0
    )

    new_login = user_input.launch()
    if new_login[1][1] == new_login[2][1]:
        add_user(new_login[0][1], new_login[1][1])
    else:
        print(Fore.RED + "\nPasswords do not match!" + Fore.WHITE)
        time.sleep(2)
        clearConsoleUp(5)
        clearLine()
        new_user()

    
if __name__ == "__main__": 
    start_cli()
    