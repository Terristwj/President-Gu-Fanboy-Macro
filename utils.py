import app
from app import auto, time

# Debugging functions
def get_cursor_location() -> None:
    wait_time = app.settings.config['time_to_get_cursor']
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
    app.settings.config['has_cursor_location'] = True
    app.settings.config['telegram_chat_coords'] = [x, y]

def update_iteration(n) -> None:
    app.settings.config['iterations'] = n

def logger():
    '''Prints current iteration'''
    app.settings.config['count'] += 1
    print(app.settings.config['count'])