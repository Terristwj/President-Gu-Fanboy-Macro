from initiate import settings
from initiate import func, util, msg_func

def main_script():
    if settings.config['has_cursor_location']:
        func.repeat(func.autoPray, settings.config['iterations'])
    else:
        util.print_cursor_location()

def telegram_chat_location(msg):
    y = input(msg)
    while y.lower() not in ['y', 'yes']:
        print("Invalid response.")
        y = input("\tOnly enter 'y' or 'yes': ")
    util.get_cursor_location()

def iteration_request(msg):
    iteration = input(msg)
    while type(iteration) != int:
        try:
            iteration = int(iteration)
        except:
            print("Invalid response.")
            iteration = input("\tEnter a number iteration: ")
    util.update_iteration(iteration)

def repeat_request(msg):
    response = input(msg)
    while response not in ['y', 'n']:
        print("Invalid response.")
        response = input("\tEnter 'Y/N': ")

    if response.lower() == 'n':
        settings.config['exit'] = True
        msg_func.print_goodbye()

