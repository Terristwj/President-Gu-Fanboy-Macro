from initiate import settings
from initiate import msg_func
import initiate

def run_tutorial():
    msg_func.print_tutorial_intro()

    msg = "\tStep 1: Type 'YES' and move your cursor quick to the chat! "
    initiate.common.telegram_chat_location(msg)
    
    msg_func.print_tutorial_cheer("Great!")
    iterate_pray()

    while not settings.config['exit']:
        iterate_pray()

def iterate_pray():
    msg = "\tStep 2: Give me iteration number: "
    initiate.common.iteration_request(msg)

    msg_func.print_tutorial_cheer("\nAwesome!")
    msg_func.print_tutorial_praying()
    initiate.common.main_script()

    msg_func.print_tutorial_complete()
    initiate.common.repeat_request("\tRepeat (Y/N)? ")