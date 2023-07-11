from app import auto, time
import initiate

# Debugging functions
def get_cursor_location() -> None:
    wait_time = initiate.settings.config['time_to_get_cursor']
    print("\nRetrieving cursor location...")
    print(f"Please wait {wait_time} seconds!")
    time.sleep(wait_time)

    cursor_location = auto.position()
    print_cursor_location(cursor_location)

    [x, y] = cursor_location
    update_cursor_location(x, y)

def print_cursor_location(cursor_location) -> None:
    print("\nCursor location:")
    print(f"{cursor_location}\n")

def update_cursor_location(x, y) -> None:
    initiate.settings.config['has_cursor_location'] = True
    initiate.settings.config['telegram_chat_coords'] = [x, y]

def update_iteration(n) -> None:
    initiate.settings.config['iterations'] = n

def logger():
    '''Prints current iteration'''
    initiate.settings.config['count'] += 1
    print(initiate.settings.config['count'])