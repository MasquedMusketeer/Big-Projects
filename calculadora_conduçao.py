mes1 = [1,3,5,7,8,10,12]
mes2 = [2]
mes3 = [4,6,9,11]

semana_dia = [8,2,3,4,5,6,7]

mes = ''
semana = ''

usr_inpt1 = int(input('insira o mes: '))
usr_inpt2 = int(input('o dia da semana de começo: '))
usr_inpt3 = float(input('e o preço unitario: '))
quantidade_meses = int(input('insira quantos meses: '))

def month_days(x):
    if x in mes1:
        dia = 31
    elif x in mes2:
        dia = 28
    elif x in mes3:
        dia = 30
    return dia

def calculo(x,w,y):
    semana = w
    preco = y

    contador = semana_dia.index(semana)
    contador_dias = x
    contadorTotal = 0
    totalconduçao = 0
    flag = 0

    while contadorTotal < contador_dias:
        if contador == 1 or contador == 2 or contador ==3:
            totalconduçao += (preco*2)
        if flag == 1 and contador == 5:
            totalconduçao += (preco*2)
            flag = 0
        elif flag == 0 and contador == 5:
            flag = 1
        contador += 1
        contadorTotal += 1
        if contador > 6:
            contador = 0
    total = round(totalconduçao, 2)
    dia_return = semana_dia.pop(contador)
    semana_dia.insert(contador,dia_return)
    result = [total, dia_return]
    return result

lista_de_resultados = []

contadorLoop = quantidade_meses
contadorInverso = 0
while contadorLoop > 0:
    if contadorLoop == quantidade_meses:
        dia = month_days(usr_inpt1)
        resultado1 = calculo(dia,usr_inpt2,usr_inpt3)
        lista_de_resultados.append(resultado1)
    else:
        dia = month_days(usr_inpt1+(contadorInverso+1))
        resultado_subseq = calculo(dia,lista_de_resultados[contadorInverso][1],usr_inpt3)
        lista_de_resultados.append(resultado_subseq)
    if contadorLoop != quantidade_meses:
        contadorInverso += 1
    contadorLoop -= 1
    
total = 0
totalmensal = []

for x in lista_de_resultados:
    for y in x:
        if x.index(y) == 0:
            total += y
            totalmensal.append(y)

print(f'resultado por mes: {totalmensal}, resultado total: {total}')