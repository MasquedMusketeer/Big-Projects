lineOfOP = []


def fullOP():
    counter = len(lineOfOP)
    while counter > 0:
        singleOP(1)
        counter -= 1
    Operations()

def singleOP(x):
    if bool(lineOfOP) == False:
        print('')
        print('>>>The list of operations is empty<<<')
        print('')
        Operations()
    else:
        print('')
        flag = x
        op = lineOfOP.pop(0)
        print(op)
        operation = op.pop(0)
        result = 0
        if operation == '+':
            for x in op:
                result += x
        elif operation == '-':
            result = op.pop(0)
            for x in op:
                result -= x
        elif operation == '*':
            result = op.pop(0)
            for x in op:
                result = result*x
        elif operation == '/':
            result = op.pop(0)
            for x in op:
                result = result/x
        print('Result of Operation: ',result)
        print('')
        if flag == 0:
            Operations()


def lineDictator(x,y):
    value = x
    flag = y
    if flag == 1:
        lineOfOP.append(value)
    elif flag == 0:
        if value == 2:
            singleOP(0)
        elif value == 3:
            fullOP()

def add():
    valueList = ["+"]
    flag = 0
    while flag == 0:
        usr_choice = input('Insert values to be added. When done, type "done":')
        if usr_choice == 'done' or usr_choice == 'Done':
            flag = 1
        else:
            valueList.append(int(usr_choice))
    lineDictator(valueList,1)
    Operations()

def sub():
    valueList = ["-"]
    flag = 0
    while flag == 0:
        usr_choice = input('Insert values to be subtracted. When done, type "done":')
        if usr_choice == 'done' or usr_choice == 'Done':
            flag = 1
        else:
            valueList.append(int(usr_choice))
    lineDictator(valueList,1)
    Operations()

def mult():
    valueList = ["*"]
    flag = 0
    while flag == 0:
        usr_choice = input('Insert values to be multiplied. When done, type "done":')
        if usr_choice == 'done' or usr_choice == 'Done':
            flag = 1
        else:
            valueList.append(int(usr_choice))
    lineDictator(valueList,1)
    Operations()

def div():
    valueList = ["/"]
    flag = 0
    while flag == 0:
        usr_choice = input('Insert values to be divided. When done, type "done":')
        if usr_choice == 'done' or usr_choice == 'Done':
            flag = 1
        else:
            valueList.append(int(usr_choice))
    lineDictator(valueList,1)
    Operations()
    
def AvailableOP():
    print('1-Addition(+)')
    print('2-Subtraction(-)')
    print('3-Multiplication(*)')
    print('4-Division(/)')
    usr_inpt3 = int(input('>>>  '))
    if usr_inpt3 == 1:
        add()
    elif usr_inpt3 == 2:
        sub()
    elif usr_inpt3 == 3:
        mult()
    elif usr_inpt3 == 4:
        div()

def Operations():
    print('Here are the operations available')
    print('1- Add operation to the line')
    print('2- Do the next operation in line')
    print('3- Do all line operations')
    print('0- Go back to main menu')
    usr_inpt2 = int(input('>>>  '))
    if usr_inpt2 == 1:
        AvailableOP()
    elif usr_inpt2 == 2:
        lineDictator(2,0)
    elif usr_inpt2 == 3:
        lineDictator(3,0)
    elif usr_inpt2 == 0:
        initialization()

def endSequence():
    print('We thank your preference, come back later!')

def MainMenu():
    usr_inpt = int(input('>>>  '))
    if usr_inpt == 0:
        endSequence()
    elif usr_inpt == 1:
        Operations()
    #elif usr_inpt == 2:
     #   Expressions()
    else:
        print('No available operation maching input, try again...')
        MainMenu()

def initialization():
    print('Welcome to the Line Calculator Project 1.0')
    print('Here are the options:')
    print('1-Operations 2-Expression 0-Exit')
    MainMenu()
    
initialization()