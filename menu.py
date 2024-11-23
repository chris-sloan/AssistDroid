from os import system


class MenuItem:
    def __init__(self, name, action):
        self.name = name
        self.action = action

def display_menu(menu_items, devices, ticket_number, ticket_description):
    system("clear")
    print("=========================================")
    print("============= AssistDroid  ==============")
    print("=========================================")
    if len(devices) > 0:
        print(f"==== Devices in Use : {devices}")
    if len(ticket_number) > 0:
        print(f"==== Current Ticket : {ticket_number}")
    if len(ticket_description) > 0:
        print(f"==== Current Ticket : {ticket_description}")
    if len(devices) > 0 or len(ticket_number) > 0 or len(ticket_description) > 0:
        print("=========================================")
    print("==== Menu")
    for i, item in enumerate(menu_items, 1):
        print(f"{i}. {item.name}")
    print("=========================================")
    
def handle_user_choice(choice, menu_items):
    if choice.lower() == 'q':
        exit()
    try:
        choice = int(choice) - 1
        if 0 <= choice < len(menu_items):
            menu_items[choice].action()
        else:
            print("Invalid option, please choose between 1 and {} or 'q' to quit.".format(len(menu_items)))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and {} or 'q' to quit.".format(len(menu_items)))