import initiate

def run_scripts():
    initiate.common.telegram_chat_location("Enter 'y' and move to telegram chat: ")
    main_scripts()

def main_scripts():
    initiate.common.iteration_request("How many iterations? ")
    initiate.common.main_script()
    initiate.common.repeat_request("Repeat (Y/N)? ")

def repeat_scripts():
    main_scripts()