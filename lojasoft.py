file = open(r'C:\Users\Masquerade\Documents\Faculdade\Python\tabela.txt', mode = 'r', encoding = 'utf-8')

tabela_de_preços = []
for item in file:
    tabela_de_preços.append(item)
file.close()
resposta_positiva = ['sim','Sim']
resposta_negativa = ['não','Não','nao','Nao']
def atualizar():
    file = open(r'C:\Users\Masquerade\Documents\Faculdade\Python\tabela.txt', mode = 'w', encoding = 'utf-8')
    for item in tabela_de_preços:
        file.write(item)
        file.write('\n')
    file.close()
def adicionar_item():
    file = open(r'C:\Users\Masquerade\Documents\Faculdade\Python\tabela.txt', mode = 'r', encoding = 'utf-8')
    flag = True
    buffer_de_itens = []
    while flag == True:
        item_a_ser_adicionado = input('Insira o nome do produto: ')
        preço_do_item = str(input('Insira o preço: '))
        enunciado = item_a_ser_adicionado + ' - R$ ' + preço_do_item
        buffer_de_itens.append(enunciado)
        continuar = input('mais algu item?(sim ou não): ')
        if continuar in resposta_positiva:
            flag = True
        elif continuar in resposta_negativa:
            flag = False
        else:
            flag = True
    for item in buffer_de_itens:
        tabela_de_preços.append(item)
    file.close()
    atualizar()
    gato2()
posição = 0
def modificar_item():
    file = open(r'C:\Users\Masquerade\Documents\Faculdade\Python\tabela.txt', mode = 'r', encoding = 'utf-8')
    buffer_de_itens_a_modificar = []
    buffer_de_transcrição = []
    item_por_extenso = ""
    for item in tabela_de_preços:
        buffer_de_itens_a_modificar.append(item.split())
    escolha_do_usuário = input('Qual produto terá o preço mudado?: ')
    flag2 = False
    for item in buffer_de_itens_a_modificar:
        for produto in item:
            if escolha_do_usuário in produto:
                flag2 = True
                novo_preço = input('Insira o novo preço: ')
                item.pop()
                item.append(novo_preço)
    if flag2 == False:
        print('Produto não encontrado')
    for item in buffer_de_itens_a_modificar:
        contador = 0
        while contador < 4:
            for produtos in item:
                processador_de_enunciado = produtos
                if produtos == novo_preço:
                    item_por_extenso += processador_de_enunciado
                    contador += 1
                else:
                    item_por_extenso += (processador_de_enunciado + ' ')
                    contador += 1
        if contador == 4:
            buffer_de_transcrição.append(item_por_extenso)
            item_por_extenso = ""
    tabela_de_preços.clear()
    for item in buffer_de_transcrição:
        tabela_de_preços.append(item)
    file.close()
    atualizar()
    gato2()
registro_de_adm = []
def login_e_senha():
    file = open(r'C:\Users\Masquerade\Documents\Faculdade\Python\registro.txt', mode = 'r', encoding = 'utf-8')
    registro_de_adm.clear()
    for login in file:
        registro_de_adm.append(login.strip('\n'))
    file.close()
def adicionar_adm():
    file = open(r'C:\Users\Masquerade\Documents\Faculdade\Python\registro.txt', mode = 'a', encoding = 'utf-8')
    login_de_input = str(input('Insira o nome do novo usuáro: '))
    senha_de_input = str(input('Insira a senha do novo usuáro: '))
    senha_confirmacao = str(input('Confirme a senha: '))
    if senha_de_input == senha_confirmacao:
        login_completo = login_de_input + ' ' + senha_de_input
        file.write('/n')
        file.write(login_completo)
    else:
        print('Senha não corresponde com a confirmação, verifique e tente novamente.')
        gato2()
    file.close()
def gato():
    inicializacao()
def gato2():
    login_correto()
def tabela():
    file = open(r'C:\Users\Masquerade\Documents\Faculdade\Python\tabela.txt', mode = 'r', encoding = 'utf-8')
    for item in file:
        print(item.strip('\n'))
    file.close()
def login_correto():
    usr_choice_3 = int(input('1-Ver tabela de preços'+'\n'+'2-alterar o preço'+'\n'+'3-adicionar um produto'+'\n'+'4-adicionar administrador novo'+'\n'+'5-Ver pedidos'+'\n'+'6-Voltar ao menu inicial'+'\n'+'Input: '))
    if usr_choice_3 == 6:
        gato()
    elif usr_choice_3 == 2:
        modificar_item()
    elif usr_choice_3 == 3:
        adicionar_item()
    elif usr_choice_3 == 1:
        tabela()
        gato2()
    elif usr_choice_3 == 4:
        adicionar_adm()
    elif usr_choice_3 == 5:
        tabela_de_pedidos()
        gato2()
def gato3():
    opçoes_do_usuario()
def tabela_de_pedidos():
    file = open(r'C:\Users\Masquerade\Documents\Faculdade\Python\pedido.txt', mode = 'r', encoding = 'utf-8')
    for item in file:
        print(item.strip('\n'))
    file.close()
def pedidos():
    file = open(r'C:\Users\Masquerade\Documents\Faculdade\Python\carrinho.txt', mode = 'r', encoding = 'utf-8')
    file2 = open(r'C:\Users\Masquerade\Documents\Faculdade\Python\pedido.txt', mode = 'a', encoding = 'utf-8')
    for item in file:
        file2.write(item)
        file2.write('\n')
    file2.write('\n')
    file.close()
    file2.close()
    file = open(r'C:\Users\Masquerade\Documents\Faculdade\Python\carrinho.txt', mode = 'w', encoding = 'utf-8')
    file.flush()
    file.close()
    #completar a funçao mais tarde
    #000000000000000000000000000000000000000000000000000000000
def total():
    file = open(r'C:\Users\Masquerade\Documents\Faculdade\Python\carrinho.txt', mode = 'r', encoding = 'utf-8')
    tudo = []
    quantidade = []
    preço_item = []
    for item in file:
        tudo.append(item)
    flag4 = 'quantidade'
    contador = len(tudo)
    while contador > 0:
        item = tudo.pop(0)
        separar = item.split()
        if flag4 == 'quantidade':
            quant = separar.pop(0)
            quantidade.append(quant)
            flag4 = 'item'
        elif flag4 == 'item':
            item = separar.pop(0)
            preço_item.append(item)
            flag4 = 'quantidade'
    print('em fase de cosntruçao')
    #000000000000000000000000000000000000000000000000000000000
def carrinho():
    file = open(r'C:\Users\Masquerade\Documents\Faculdade\Python\carrinho.txt', mode = 'w', encoding = 'utf-8')
    flag3 = True
    buffer_de_pedido = []
    print('Escreva a quantidade e o nome do produto separados por espaço, quando finalizar o pedido, escreva "finalizar":')
    while flag3 == True:
        pedido = input('-')
        if pedido == 'finalizar':
            flag3 = False
        else:
            buffer_de_pedido.append(pedido)
    if flag3 == False:
        for item in buffer_de_pedido:
            file.write(item)
            file.write('\n')
    file.close()
    pedidos()
    opçoes_do_usuario()
def opçoes_do_usuario():
    usr_choice_2 = input('Gostaria de saber o menu?(sim/não): ')
    if usr_choice_2 in resposta_positiva:
        tabela()
        carrinho_option = input('Gostaria de fazer seu pedido?(sim/não): ')
        if carrinho_option in resposta_positiva:
            carrinho()
        else:
            gato3()
    elif usr_choice_2 in resposta_negativa:
        gato()
def inicializacao():
    usr_choice = input(f'Bom dia. Usuário ou administrador? ')
    if usr_choice == 'usuário' or usr_choice == 'Usuário' or usr_choice == 'usuario' or usr_choice == 'Usuario':
        opçoes_do_usuario()
    elif usr_choice == 'administrador' or usr_choice == 'Administrador' or usr_choice == 'adm':
        login = str(input('Login: '))
        password = str(input('Senha: '))
        login_completo = login+" "+password
        login_e_senha()
        for login in registro_de_adm:
            if login_completo == login:
                login_correto()
            else:
                print('Credenciais informadas estão incorretas, verifique e tente novamente.')
                gato()
    elif usr_choice == 'sair' or usr_choice == 'Sair':
        print('Obrigado e volte sempre!')
inicializacao()