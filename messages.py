def print_title():
    msg = "Auto Prayer Bot for President Jason Gu Bot"
    print("=" * (len(msg)+4))
    print("= " + msg + " =")
    print("=" * (len(msg)+4))

def print_tutorial_intro():
    print("\nAlright! Follow my instructions and you won't get lost!")
    print('''\tStep 1: Upon entering 'YES', hover you cursor to the telegram chat area
        Step 2: Please tell me how many times to pray. Enter a number.
        Step 3: Do you want to continue? 'Y/N'
        Step 3.5: If 'Y', enter a number again!
    ''')
    print("Okay let's go!")

def print_tutorial_praying():
    print("\tRunning auto praying.")
    print("\tMove your course to the far top-left to FAILSAFE exit.")


def print_tutorial_cheer(msg):
    print(msg)

def print_tutorial_complete():
    print("\nCompleted praying session :)")

def print_tutorial_repeat():
    print("\nLooks like we are not done praying.")
    print("Back to step 2 :D")

def print_goodbye():
    print("\nThank you for auto praying with me.")
    print("I will pray harder next time!")


def my_script():
    print('''
                Auto Prayer Bot for President Jason Gu Bot.
            \n  Follow my instructions and you won't get lost!
            \n  Step 1: Upon entering 'YES', move you cursor to the telegram chat area
            \n  Step 2: Please tell me how many times to pray. Enter a number.
            \n  Step 3: Do you want to continue? 'Y/N'
            \n  Step 3.5: If 'Y', enter a number again!
            \n
            \n  Okay let's go!
            \n  Step 1: Type 'YES' and move your cursor quick to the chat!
            \n
            \n  Great!
            \n  Step 2: Give me iteration number:
            \n
            \n  Awesome!
            \n  Running auto praying. Move your course to the far top-left to FAILSAFE exit
            \n
            \n  Completed praying session :)
            \n  Do you want to repeat prayers? 'Y/N'
            \n
            \n  Looks like we are not done.
            \n  Back to step 2 :D
            \n
            \n  Thank you for auto praying with me...
            \n  I will pray harder next time.
            ''')