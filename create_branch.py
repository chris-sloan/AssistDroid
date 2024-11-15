import subprocess
import os, re

def is_git_repository():
    return os.path.exists(".git")

def check_for_uncommitted_changes():
    return subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)


def get_branch_details():
    ticket_number = get_valid_details("Enter the ticket number: ", r"[^a-zA-Z0-9_-]")
    branch_description = get_valid_details("Enter a brief description of the changes: ", r"[^a-zA-Z0-9_-]")
    return ticket_number, branch_description

def get_valid_details(message, regex):
    while True:
        user_input = input(message)
        if not user_input.strip():
            print("Input cannot be empty. Please try again.")
            continue
        # Replace invalid characters with underscores
        return re.sub(regex, "_", user_input)

def create_and_checkout_branch(ticket_number, branch_description):
    branch_name = f"{ticket_number}_-_{branch_description.replace(' ', '_')}"
    result = subprocess.run(["git", "checkout", "-b", branch_name], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error received: {result.stderr}. Press enter to continue.")
        input()
        return None, None

    print(f"Created and checked out branch: {branch_name}. Press enter to continue.")
    input()
    return ticket_number, branch_description

def create_git_branch():
    """
    We do some simple validation before creating the branch here.
    We check for a git repo, and offer to init one if it does not exist.
    We check for uncommited changes, and offer to stash them.
    Only then do we try to get some user input.
    """
    if not is_git_repository():
        print(f"Current directory is not a Git repository.")
        if input("Do you want to initialize a Git repository here? (y/n): ").lower() == 'y':
            subprocess.run(["git", "init"])
        else:
            print("Aborting branch creation. Press enter to continue.")
            input()
            return None, None

    uncommited_changes = check_for_uncommitted_changes()
    if uncommited_changes.returncode != 0:
        print(f"Error received: {uncommited_changes.stderr}. Press enter to continue")
        input()
        return None, None
    elif uncommited_changes.stdout.strip():
        if input("Please commit or stash your changes before creating a new branch. Do you want to stash here? (y/n): ").lower() == 'y':
            subprocess.run(["git", "stash"])
        else:
            print("Aborting branch creation. Press enter to continue.")
            input()
            return None, None

    ticket_number, branch_description = get_branch_details()
    return create_and_checkout_branch(ticket_number, branch_description)

if __name__ == "__main__":
    ticket_number, branch_description = create_git_branch()
    if ticket_number and branch_description:
        print(f"Created branch: {ticket_number} - {branch_description}")