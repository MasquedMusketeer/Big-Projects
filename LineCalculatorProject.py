lineOfOP = []

def Expressions():
    print('<< Type the mathematical expression to be validated: >>')
    usr_inpt = input('>>> ')
    processingList = list(usr_inpt)
    valueList = ['(',')','{','[',']','}']
    validPairs = ['()','[]','{}']
    valueCompare = []
    comparingStack = []
    counter = len(processingList)
    while counter > 0:
        value = processingList.pop(0)
        if value in valueList:
            valueCompare.append(value)
        else:
            processingList.append(value)
        counter -= 1
    counterCompare = len(valueCompare)/2
    compareIndex = counterCompare
    while counterCompare > 0:
        transition = valueCompare.pop(0)
        comparingStack.append(transition)
        counterCompare -= 1
    validationFlag = 0
    invalidationFlag = 0
    comparingStack.reverse()
    validationCounter = 0
    for value in valueCompare:
        stackTop = comparingStack.pop(0)
        if stackTop+value in validPairs and validationCounter == validPairs.index(stackTop+value):
            validationFlag += 1
            compareIndex -= 1
        else:
            invalidationFlag += 1
            compareIndex -= 1
        validationCounter += 1
    if invalidationFlag == 0:
        print('>>>  The expression is valid.  <<<')
        MainMenu()
    elif invalidationFlag >= 1:
        print('>>>  The expression is not valid.  <<<')
        MainMenu()

def fullOP():
    counter = len(lineOfOP)
    while counter > 0:
        singleOP(1)
        counter -= 1
    Operations()

def singleOP(x):
    if bool(lineOfOP) == False:
        print('')
        print('>>>  The list of operations is empty  <<<')
        print('')
        Operations()
    else:
        print('')
        flag = x
        op = lineOfOP.pop(0)
        print('>>> ',op," <<<")
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
        print('>>> Result of Operation: ',result,' <<<')
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
    print('<< Insert values to be added. When done, type "done" >>')
    valueList = ["+"]
    flag = 0
    while flag == 0:
        usr_choice = input('>>>  ')
        if usr_choice == 'done' or usr_choice == 'Done':
            flag = 1
        else:
            valueList.append(int(usr_choice))
    lineDictator(valueList,1)
    Operations()

def sub():
    print('<< Insert values to be subtracted. When done, type "done" >>')
    valueList = ["-"]
    flag = 0
    while flag == 0:
        usr_choice = input('>>>  ')
        if usr_choice == 'done' or usr_choice == 'Done':
            flag = 1
        else:
            valueList.append(int(usr_choice))
    lineDictator(valueList,1)
    Operations()

def mult():
    print('<< Insert values to be multiplyed. When done, type "done" >>')
    valueList = ["*"]
    flag = 0
    while flag == 0:
        usr_choice = input('>>>  ')
        if usr_choice == 'done' or usr_choice == 'Done':
            flag = 1
        else:
            valueList.append(int(usr_choice))
    lineDictator(valueList,1)
    Operations()

def div():
    print('<< Insert values to be divided. When done, type "done" >>')
    valueList = ["/"]
    flag = 0
    while flag == 0:
        usr_choice = input('>>>  ')
        if usr_choice == 'done' or usr_choice == 'Done':
            flag = 1
        else:
            if int(usr_choice) == 0:
                print('>>>  Divisions by 0 are not permited.  <<<')
            else:
                valueList.append(int(usr_choice))
    lineDictator(valueList,1)
    Operations()
    
def AvailableOP():
    print('----------------------------------------------------')
    print('|                  1-Addition(+)                   |')
    print('|                 2-Subtraction(-)                 |')
    print('|                3-Multiplication(*)               |')
    print('|                  4-Division(/)                   |')
    print('----------------------------------------------------')
    usr_inpt3 = (input('>>>  '))
    if usr_inpt3 == '1':
        add()
    elif usr_inpt3 == '2':
        sub()
    elif usr_inpt3 == '3':
        mult()
    elif usr_inpt3 == '4':
        div()
    else:
        print('No available operation matching input, try again...')
        AvailableOP()

def Operations():
    print('----------------------------------------------------')
    print('|       Here are the operations available          |')
    print('|        1- Add operation to the line              |')
    print('|        2- Do the next operation in line          |')
    print('|        3- Do all line operations                 |')
    print('|        0- Go back to main menu                   |')
    print('----------------------------------------------------')
    usr_inpt2 = (input('>>>  '))
    if usr_inpt2 == '1':
        AvailableOP()
    elif usr_inpt2 == '2':
        lineDictator(2,0)
    elif usr_inpt2 == '3':
        lineDictator(3,0)
    elif usr_inpt2 == '0':
        initialization()
    else:
        print('>>>> No available operation matching input, try again... <<<<')
        Operations()

def endSequence():
    print('----------------------------------------------------')
    print('|    We thank your preference, come back later!    |')
    print('----------------------------------------------------')

def MainMenu():
    print('----------------------------------------------------')
    print('|              Here are the options:               |')
    print('|         1-Operations 2-Expression 0-Exit         |')
    print('----------------------------------------------------')
    usr_inpt = (input('>>>  '))
    if usr_inpt == '0':
        endSequence()
    elif usr_inpt == '1':
        Operations()
    elif usr_inpt == '2':
        Expressions()
    else:
        print('-----------------------------------------------------')
        print('|No available operation matching input, try again...|')
        print('-----------------------------------------------------')
        MainMenu()

def initialization():
    print('----------------------------------------------------')
    print('|     Welcome to the Line Calculator Project 1.1   |')
    print('----------------------------------------------------')
    MainMenu()
    
initialization()