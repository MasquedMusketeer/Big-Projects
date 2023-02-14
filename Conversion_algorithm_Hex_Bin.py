def D_to_B():
    value_list = ['0','1']
    value_algarithm = []
    conversion_number = int(input('Insira o Decimal para conversão: '))
    result = conversion_number
    bin_value_conversion = ''

    def conversion(x):
        result = x
        value_buffer = 0
        while result > 0:
            result -= 2
            value_buffer += 1
        if result < 0:
            result += 2
            value_buffer -= 1
        if result > 1:
            bin_value_conversion = value_list.pop(result)
            value_list.insert(result, bin_value_conversion)
            value_algarithm.append(bin_value_conversion)
        else:
            bin_value_conversion = result
            value_algarithm.append(bin_value_conversion)
        gato(value_buffer)
    def gato(y):
        value_buffer = y
        result = 0
        if value_buffer >= 2:
            result = value_buffer
        else:
            bin_value_conversion = value_list.pop(value_buffer)
            value_list.insert(value_buffer, bin_value_conversion)
            value_algarithm.append(bin_value_conversion)
        if result == value_buffer:
            conversion(result)

    conversion(result)

    bin_value_converted = ''
    counter = len(value_algarithm)
    while counter > 0:
        algarithm = value_algarithm.pop()
        bin_value_converted += str(algarithm)
        counter -= 1
    result(bin_value_converted)

def B_to_D(f,v):
    if f == 0:
        flag = True
    elif f == 1:
        flag = False

    if flag == True:
        usr_inpt = input('Insira o Hexadecimal para conversão: ')
    elif flag == False:
        usr_inpt = v

    algarithm_separation = list(usr_inpt)
    counter = len(algarithm_separation)
    while counter > 0:
        x = algarithm_separation.pop(0)
        y = int(x)
        algarithm_separation.append(y)
        counter -= 1

    exponential_counter = len(algarithm_separation) - 1
    total = 0

    for x in algarithm_separation:
        if x == 1:
            result = 2**exponential_counter
            total += result
        exponential_counter -= 1
    
    if flag == True:
        result(total)
    elif flag == False:
        D_to_H(total)

def D_to_H():
    value_list = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    value_algarithm = []
    conversion_number = int(input('Insira o Decimal para conversão: '))
    result = conversion_number
    hex_value_conversion = ''

    def conversion(x):
        result = x
        value_buffer = 0
        while result > 0:
            result -= 16
            value_buffer += 1
        if result < 0:
            result += 16
            value_buffer -= 1
        if result > 9:
            hex_value_conversion = value_list.pop(result)
            value_list.insert(result, hex_value_conversion)
            value_algarithm.append(hex_value_conversion)
        else:
            hex_value_conversion = result
            value_algarithm.append(hex_value_conversion)
        gato(value_buffer)
    def gato(y):
        value_buffer = y
        result = 0
        if value_buffer >= 16:
            result = value_buffer
        else:
            hex_value_conversion = value_list.pop(value_buffer)
            value_list.insert(value_buffer, hex_value_conversion)
            value_algarithm.append(hex_value_conversion)
        if result == value_buffer:
            conversion(result)

    conversion(result)

    hex_value_converted = ''
    counter = len(value_algarithm)
    while counter > 0:
        algarithm = value_algarithm.pop()
        hex_value_converted += str(algarithm)
        counter -= 1

    result(hex_value_converted)

def H_to_D(f,v):
    if f == 0:
        flag = True
    elif f == 1:
        flag = False

    value_list = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    
    if flag == True:
        usr_inpt = input('Insira o Hexadecimal para conversão: ')
    elif flag == False:
        usr_inpt = v
    algarithm_separation = list(usr_inpt)
    for x in range(len(algarithm_separation)):
        algarithm_separation[x] = algarithm_separation[x].upper()

    total = 0
    last_algarithm_addition = 0
    last_algarithm = algarithm_separation.pop()
    for x in value_list:
        if x == last_algarithm:
            last_algarithm_addition = value_list.index(x)

    exponential_counter = len(algarithm_separation)

    for x in algarithm_separation:
        for y in value_list:
            if x == y:
                result = 16**exponential_counter
                total += (result * value_list.index(y))
        exponential_counter -= 1

    converted = total + last_algarithm_addition
    if flag == True:
        result(converted)
    elif flag == False:
        D_to_B(converted)

def result(x):
    print("O valor convertido é:", x)
    initialization()

def H_to_B():
    usr_inpt = input('Insira o Hexadecimal para conversão: ')
    H_to_D(1,usr_inpt)

def B_to_H():
    usr_inpt = input('Insira o Hexadecimal para conversão: ')
    B_to_D(1,usr_inpt)

def Hex_Bin():
    conversion_inpt_selector = int(input('1-Binário -> Hexadecimal  2-Hexadecimal -> Binário  : '))
    if conversion_inpt_selector == 2:
        H_to_B()
    elif conversion_inpt_selector == 1:
        B_to_H()


def Bin():
    conversion_inpt_selector = int(input('1-Binário -> Decimal  2-Decimal -> Binário  : '))
    if conversion_inpt_selector == 1:
        B_to_D(0,0)
    elif conversion_inpt_selector == 2:
        D_to_B()

def Hex():
    conversion_inpt_selector = int(input('1-Hexadecimal -> Decimal  2-Decimal -> Hexadecimal  : '))
    if conversion_inpt_selector == 1:
        H_to_D(0,0)
    elif conversion_inpt_selector == 2:
        D_to_H()


def initialization():
    conversion_inpt_selector = int(input('1-Binário  2-Hexadecimal  3-Hex-Bin  4-Exit  : '))
    if conversion_inpt_selector == 1:
        Bin()
    elif conversion_inpt_selector == 2:
        Hex()
    elif conversion_inpt_selector == 3:
        Hex-Bin()
    elif conversion_inpt_selector == 4:
        print('Goodbye!')










initialization()