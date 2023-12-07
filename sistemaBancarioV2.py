usuarios = []
limiteQtdSaques = 3
limiteValorSaque = 500.00
numContaAtual = 1

#EXTRATO CONTA
def extratoConta(idUser, idConta):
    print(f'        {str(" EXTRATO ").center(40, "-")}\n')

    for item in usuarios[idUser]['contas'][idConta]['extrato']:
        if item['transacao'] == 'saque':
            print(f"{str(item['transacao']) + 3*' '} : - R$ {round(float(item['valor']), 2)}")
        else:
            print(f"{str(item['transacao'])} :   R$ {round(float(item['valor']), 2)}")

    print(f"\nSaldo conta: R$ {round(usuarios[idUser]['contas'][idConta]['saldo da conta'], 2)}")     
    print('\n\n')
    menuTransacoes(idUser, idConta)

#SAQUE
def saqueConta(idUser, idConta):
    global saldoConta
    global qtdSaques
    valor = float(input(f"""
            {str(" SAQUE ").center(40, "-")}  
        
    Digite o valor que deseja sacar => R$ """))
    if usuarios[idUser]['contas'][idConta]['saldo da conta'] < valor:
        print('Saldo indisponivel')
    elif valor > limiteValorSaque:
        print(f'''
            Valor maximo de R$ {limiteValorSaque} atingido !!
            Tente novamente
            ''')
    elif usuarios[idUser]['contas'][idConta]['qtd saques diarios'] >= limiteQtdSaques:
        print(f'''
            Limite de {limiteQtdSaques} saques diarios atingido !!
            Tente novamente amanha
            ''')
    else:
        usuarios[idUser]['contas'][idConta]['saldo da conta'] -= valor
        novo = {
            'transacao' : 'saque',
            'valor' : valor
        }
        usuarios[idUser]['contas'][idConta]['extrato'].append(novo)
        print('Saque realizado com sucesso !!')
        usuarios[idUser]['contas'][idConta]['qtd saques diarios'] += 1
        menuTransacoes(idUser, idConta)

#DEPOSITO
def depositoConta(idUser, idConta):
    global saldoConta
    valor = float(input(f"""
    {str(" DEPOSITO ").center(40, "-")}

Digite o valor que deseja depositar => R$ """))
            
    usuarios[idUser]['contas'][idConta]['saldo da conta'] += valor
    novo = {
        'transacao' : 'deposito',
        'valor' : valor
    }
        
    usuarios[idUser]['contas'][idConta]['extrato'].append(novo)
    print('Deposito realizado com sucesso !!')
    menuTransacoes(idUser, idConta)

#CRIAR USUARIO
def criarUsuario():
    nome = input(f"""
        {str(" CRIAR USUARIO ").center(40, "-")}
    

Digite seu nome completo => """)
    
    dataNasc = input("Digite sua data de nascimento (ex : dd/mm/yyyy) => ")

    cpf = input("Digite seu CPF => ").replace('.', '').replace('-', '')

    logradouro = input("Digite o logradouro da sua residencia => ") 

    num = input("Digite o numero da sua residencia => ")

    bairro = input("Digite seu bairro => ")

    cidade = input('Digite sua cidade => ')

    siglaEstado = input("Digite a sigla do seu estado (ex : RJ) =>")

    for user in usuarios:
        if user['cpf'] == cpf:
            print('CPF ja cadastrado !!\nDigite um CPF que nao esteja cadastrado')
            return False

    novo = {
        'nome' : nome,
        'data de nascimento' : dataNasc,
        'cpf' : cpf,
        'endereco': f'{logradouro},{num} - {bairro} - {cidade}/{siglaEstado}',
        'contas' : []
    }
    usuarios.append(novo)


#CRIAR CONTA
def criarConta():
    
    cpf = input(f"""
        {str(" CRIAR CONTA ").center(40, "-")}
    

Digite seu cpf => """).replace('.', '').replace('-', '')
    
    check = False
    attUser = 0
    for user in usuarios:
        if user['cpf'] == cpf:
            check = True
            attUser = usuarios.index(user)
    
    if check:
        global numContaAtual

        novo = {
            'agencia' : '0001',
            'numero da conta' : numContaAtual,
            'saldo da conta' : 0.0,
            'qtd saques diarios': 0,
            'extrato' : []
        }

        usuarios[attUser]['contas'].append(novo)

        numContaAtual+=1
        print('Conta criada com sucesso !!')
    else:
        print('CPF invalido ou nao cadastrado!\nTente novamente')


#ACESSAR CONTA
def acessarConta():
    cpf = input(f"""
        {str(" ACESSAR CONTA ").center(40, "-")}
    

Digite seu cpf => """).replace('.', '').replace('-', '')
    check = False
    indexUser = 0
    indexConta = 0
    for user in usuarios:
        if user['cpf'] == cpf:
            check = True
            indexUser = usuarios.index(user)
            for conta in usuarios[indexUser]['contas']:
                for chave, valor in conta.items():
                    print(f'{chave}: {valor}')
            nConta = int(input('Digite o numero da conta que deseja acessar => '))

            for conta in usuarios[indexUser]['contas']:
                if nConta == conta['numero da conta']:
                    indexConta = usuarios[indexUser]['contas'].index(conta)

            break
        else:
            continue
    if check:
        menuTransacoes(indexUser, indexConta)
    else:
        print('CPF invalido ou nao cadastrado!\nTente novamente')
    


def menuTransacoes(indexUser, indexConta):
    try:
        opcao = input(f"""
            {str(" MENU ").center(40, "-")}
        
        Opcoes:

        [1] Extrato
        [2] Saque
        [3] Deposito
        [0] Sair

    Digite uma opcao => """)

        
        if int(opcao) == 1:
            extratoConta(indexUser, indexConta)
            return True
        

        elif int(opcao) == 2:
            saqueConta(indexUser, indexConta)
            return True

        
        elif int(opcao) == 3:
            depositoConta(indexUser, indexConta)
            return True

        elif int(opcao) == 0:
            return False
        else:
            print('Digite uma opcao valida !')
    except:
        print("Digite uma opcao valida !!")




def menuInicial():
    try:
        opcao = input(f"""
            {str(" LOGIN BANCO ").center(40, "-")}
        
        Opcoes:

        [1] Criar usuario
        [2] Criar conta
        [3] Acessar conta
        [0] Sair

    Digite uma opcao => """)
        
        if int(opcao) == 1:
            criarUsuario()
            return True
            

        elif int(opcao) == 2:
            criarConta()
            return True

            
        elif int(opcao) == 3:
            acessarConta()
            return True
        elif int(opcao) == 0:
            return False
        else:
            print('Digite uma opcao valida')
    except:
        print('Digite uma opcao valida')
    




while True:    
    if menuInicial():
        continue
    else:
        break


    