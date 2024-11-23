from os import system
from os import path
import subprocess
import sys

sys.path.append(path.dirname(path.abspath(__file__)))
from menu import MenuItem
import menu, android_helper

def format_json():
    # Over time we should give the user some idea of what's in the clipboard.
    system("clear")
    result = subprocess.run(['pbpaste'], capture_output=True, text=True)
    if result.returncode == 0:
        pasteText = result.stdout
        print(f"Success : {pasteText}")
        print("-----")
        formatted = subprocess.run(['jq'], input=pasteText, capture_output=True, text=True)
        print(f"Success : {formatted.stdout}")
        print("-----")
        copied = subprocess.run(['pbcopy'], input=formatted.stdout, capture_output=True, text=True)
        print(f"Success : {formatted.stdout}")
        print("-----")
        input("Press enter to return to menu")
        return result
    else:
        system("clear")
        print(f"Error: Could not format json : {result.stderr}")
        input("Press enter to return to menu")
        return 
    
def __return_to_main():
    android_helper.display_menu()

def display_menu(devices, ticket_number, ticket_description):
    system("clear")

    menu_items = [
        MenuItem("Format Json", format_json),    
        MenuItem("Back to Main Menu", __return_to_main),    
        ]

    while True:
        menu.display_menu(menu_items, devices, ticket_number, ticket_description)
        choice = input("Select an option (1-{} or 'q' to quit): ".format(len(menu_items)))
        menu.handle_user_choice(choice, menu_items)
    
def main():
    display_menu([], "", "")
    
if __name__ == "__main__":
    main()
