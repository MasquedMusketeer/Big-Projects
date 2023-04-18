














def endSequence():
    print('We thank your preference, come back later!')

def MainMenu():
    initialization()

def initialization():
    print('Welcome to the Line Calculator Project 1.0')
    print('Here are the options:')
    usr_inpt = int(input('1-Operations 2-Expression 0-Exit'))
    if usr_inpt == 0:
        endSequence()
    elif usr_inpt == 1:
        Operations()
    elif usr_inpt == 2:
        Expressions()
    else:
        print('No available operation maching input, try again...')
        MainMenu()