from app import auto

# Time of pause after each PyAutoGUI call:
# auto.PAUSE = 1

# Mouse to upper-left abort program
auto.FAILSAFE = True

# Debug configs
config = {
    # First run: Cursor location
    'has_cursor_location': False,
    'time_to_get_cursor': 5,    # Editable

    # Second run: Configurations
    'telegram_chat_coords': [0, 0],
    'iterations': 0,
    'count': 0,
    'delay_seconds': 0, # Editable

    # Debugger
    'is_logged': False, # Editable

    # Controls
    'exit': False
}