from app import auto, time
import initiate

def repeat(func, n: int) -> None:
    '''Repeats for a function'''
    for _ in range(n):
        add_delay()
        func()

def autoPray() -> None:
    '''Auto pray'''
    [x, y] = initiate.settings.config['telegram_chat_coords']
    
    auto.click(x, y)
    auto.typewrite("/pray")
    auto.press("enter")
    if initiate.settings.config['is_logged']: initiate.util.logger()

def add_delay() -> None:
    '''Delay seconds'''
    time.sleep(initiate.settings.config['delay_seconds'])

