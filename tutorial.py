from app import util, script, settings, messages

def run_tutorial():
    messages.print_tutorial_intro()

    msg = "\tStep 1: Type 'YES' and move your cursor quick to the chat! "
    script.script_telegram_chat_location(msg)
    
    messages.print_tutorial_cheer("Great!")
    msg = "\tStep 2: Give me iteration number: "
    script.script_iteration_request(msg)

    messages.print_tutorial_cheer("\nAwesome!")
    messages.print_tutorial_praying()
    script.main_script()

    messages.print_tutorial_complete()
    script.script_repeat_request("\tRepeat (Y/N)? ")

    while not settings.config['exit']:
        messages.print_tutorial_repeat()
        msg = "\tStep 2: Give me iteration number:"
        script.script_iteration_request(msg)

        script.main_script()
        messages.print_tutorial_praying()
        
        messages.print_tutorial_complete()
        script.script_repeat_request("Repeat (Y/N)? ")