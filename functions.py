import app
from app import auto, time

def repeat(func, n: int) -> None:
    '''Repeats for a function'''
    for _ in range(n):
        add_delay()
        func()

def autoPray() -> None:
    '''Auto pray'''
    [x, y] = app.settings.config['telegram_chat_coords']
    
    auto.click(x, y)
    auto.typewrite("/pray")
    auto.press("enter")
    if app.settings.config['is_logged']: app.util.logger()

def add_delay() -> None:
    '''Delay seconds'''
    time.sleep(app.settings.config['delay_seconds'])

