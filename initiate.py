# Settings
from app import settings

# Functions
import functions.functions as func
import functions.utils as util
import functions.messages as msg_func

# Scripts
import scripts.common as common
import scripts.main as main
from scripts.tutorial import run_tutorial

def startup():
    msg_func.print_title()
    enable_tutorial = input("Do you need a tutorial (Y/N)? ")
    while enable_tutorial.lower() not in ['y', 'n']:
        print("Invalid response.")
        enable_tutorial = input("\tEnter 'Y/N': ")
    
    if enable_tutorial.lower() == 'y':
        run_tutorial()
    else:
        main.run_scripts()

    while not settings.config['exit']:
        main.repeat_scripts()