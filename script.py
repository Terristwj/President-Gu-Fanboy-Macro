from app import func, util, settings, messages, run_tutorial

def initiate_startup():
    messages.print_title()
    enable_tutorial = input("Do you need a tutorial (Y/N)? ")
    while enable_tutorial not in ['y', 'n']:
        print("Invalid response.")
        enable_tutorial = input("\tEnter 'Y/N': ")
    
    if enable_tutorial.lower() == 'y':
        run_tutorial()
    else:
        run_scripts()

    while not settings.config['exit']:
        repeat_scripts()

def run_scripts():
    script_telegram_chat_location("Enter 'y' and move to telegram chat: ")
    script_iteration_request("How many iterations? ")
    main_script()
    script_repeat_request("Repeat (Y/N)? ")

def repeat_scripts():
    script_iteration_request("How many iterations? ")
    main_script()
    script_repeat_request("Repeat (Y/N)? ")

def script_telegram_chat_location(msg):
    y = input(msg)
    while y.lower() not in ['y', 'yes']:
        print("Invalid response.")
        y = input("\tOnly enter 'y' or 'yes': ")
    util.get_cursor_location()

def script_iteration_request(msg):
    iteration = input(msg)
    while type(iteration) != int:
        try:
            iteration = int(iteration)
        except:
            print("Invalid response.")
            iteration = input("\tEnter a number iteration: ")
    util.update_iteration(iteration)

def main_script():
    if settings.config['has_cursor_location']:
        func.repeat(func.autoPray, settings.config['iterations'])
    else:
        util.print_cursor_location()

def script_repeat_request(msg):
    response = input(msg)
    while response not in ['y', 'n']:
        print("Invalid response.")
        response = input("\tEnter 'Y/N': ")

    if response.lower() == 'n':
        settings.config['exit'] = True
        messages.print_goodbye()

