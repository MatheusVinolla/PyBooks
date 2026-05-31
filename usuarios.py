from padrao import *

def tela_inicial():
    msg = r"""
 _                     _
| |                   (_)
| |       ___    __ _  _  _ __
| |      / _ \  / _` || || '_ \
| |____ | (_) || (_| || || | | | _   _   _
|______| \___/  \__, ||_||_| |_|(_) (_) (_)
                 __/ |
                |___/
    """
    print(f"\033[1m{msg}\033[m")
    linha()

def tela_final():
    msg = r"""   
                                                              _____   __  __
    /\                                                 /\    |  __ \ |  \/  |
   /  \     ___   ___  ___  ___   ___     ______      /  \   | |  | || \  / |
  / /\ \   / __| / _ \/ __|/ __| / _ \   |______|    / /\ \  | |  | || |\/| |
 / ____ \ | (__ |  __/\__ \\__ \| (_) |             / ____ \ | |__| || |  | |
/_/    \_\ \___| \___||___/|___/ \___/             /_/    \_\|_____/ |_|  |_|
    """
    print(f"\033[1m{msg}\033[m")
    linha()


def tela_crud():
    msg = r"""
 __  __             _                      _____  _____   _    _  _____
|  \/  |           | |                    / ____||  __ \ | |  | ||  __ \
| \  / |  ___    __| |  ___     ______   | |     | |__) || |  | || |  | |
| |\/| | / _ \  / _` | / _ \   |______|  | |     |  _  / | |  | || |  | |
| |  | || (_) || (_| || (_) |            | |____ | | \ \ | |__| || |__| |
|_|  |_| \___/  \__,_| \___/              \_____||_|  \_\ \____/ |_____/
    """
    print(f"\033[1m{msg}\033[m")
    linha()


def caixa_login():
    print("""\033[1;33m
    ____________________________
    |  Usuário: Nome de Acesso |
    |  Senha:  Senha de Acesso |
    |     *****************    |
    |    OBS:Digite apenas 0   |
    |   para sair em ambas as  |
    |     caixas de texto      |
    |__________________________|
    \033[m""", end="")


def telao(msg):
    limpar()
    tela_crud()
    print(f"\033[1;33m <<< MODO {msg.upper()} >>> \033[m")


def start(banco):
    opcao = 0
    while(opcao != 9):
        limpar()
        tela_final()
        menus()
        opcao = verificar(input(),[1,2,3,4,5,6,7,8])
        #Cadastrar","Atualizar","Pesquisar","Deletar USUÁRIOS
        #Cadastrar","Atualizar","Pesquisar","Deletar LIVROS
        
        match(opcao):
            #LIVRO
            case 1: #CADASTRAR
                telao("cadastrar livro")
                cadastrar_livro(banco)
                continuar()
            
            case 2: #ATUALIZAR
                telao("atualizar livro")
                atualizar_livro()
                continuar()
            case 3: #PESQUISAR
                telao("pesquisar livro")
                pesquisar_livro()
                continuar()
            case 4: #DELETAR
                telao("deletar livro")
                deletar_livro()
                continuar()
            #USUÁRIOS
            case 5: #CADASTRAR
                telao("cadastrar usuário")
                cadastrar_usuario()
                continuar()
            case 6: #ATUALIZAR
                telao("atualizar usuário")
                atualizar_usuario()
                continuar()
            case 7: #PESQUISAR
                telao("pesquisar usuário")
                pesquisar_usuario()
                continuar()
            case 8: #DELETAR
                telao("deletar usuário")
                deletar_usario()
                continuar()


def cadastrar_livro(banco_de_dados):
    from time import sleep
    dados = []
    padrao = ["ISBN","TITULO","AUTOR","ANO","PRECO","ESTANTE","TEMAS"]
    dados.insert(0 ,input("Insira o ISBN-10 do livo: "))
    dados.insert(0 ,input("Insira o TÍTULO do livro: "))
    dados.insert(0 ,input("Insira o/a AUTOR/A do livro: "))
    dados.insert(0 ,input("Insira o ANO do livro: "))
    dados.insert(0 ,input("Insira o PREÇO do livro: "))
    dados.insert(0 ,input("Insira a ESTANTE do livro: "))
    dados.insert(0 ,input("Insira o TEMA do livro: "))
    """
    for x in range(7):
        if x == 0:
            banco_de_dados[padrao[0]] = dados[0] 
        banco_de_dados[padrao[0]][padrao[x]] = dados[x]
    """
    processar("cadastro de livro")
    

def cadastrar_usuario():
    user = input("Insira o nome do usuário: ")
    senha = input("Insira a senha do usuário: ")
    processar("cadastro de usuario")


def atualizar_usuario():
    procura = input("Insira o nome do usuário para atualizar: ")
    processar("Usuário encontrado")
    print("Insira os novos dados de:")
    user = input("Usuário: ")
    senha = input("Senha: ")
    processar("atualização de usuario")


def pesquisar_usuario():
    procura = input("Insira o nome do usuário para pesquisar: ")
    processar("Usuário encontrado")
    print(f"""
    Usuário: {procura}
    Senha: 1234
    """)

##################################################
#LIVROS

def deletar_livro():
    procura = input("Insira o nome do Livro para deletar: ")
    processar("Livro encontrado")
    processar("Deleção de Livro")


def atualizar_livro():
    procura = input("Insira o nome do Livro para atualizar: ")
    processar("Livro encontrado")
    print("Insira os novos dados de:")
    
    codigo = input("ISBN-10: ")
    titulo = input("TÍTULO: ")
    autor = input("AUTOR/A: ")
    ano = input("ANO: ")
    preco = input("PREÇO: ")
    estante = input("ESTANTE: ")
    tema = input("TEMA: ")  
    processar("atualização de Livro")


def pesquisar_livro():
    procura = input("Insira o nome do Livro para pesquisar: ")
    processar("Livro encontrado")
    padrao = ["ISBN","TITULO","AUTOR","ANO","PRECO","ESTANTE","TEMAS"]
    outro = ["1234",f"{procura}","J.K Rowling",123.50,"Infanto Juvenil",'Magia']
    for i,e in enumerate(padrao):
        print(f"{e}: {outro[i]}")


def login(banco):
    usuario = senha = msg = ""
    while (usuario != "0") and (senha != "0"): #sairá quando digitar 0 e 0 na senha e no usuario
        limpar()
        tela_inicial()
        caixa_login()
        print(msg, end="" if len(msg) == 0 else "\n")
        usuario = input("\n\tUsuário >>> ")
        senha = input("\tSenha   >>> ")
        achou_user = False
        achou_senha = False
        for e in banco:
            if e == usuario:
                achou_user = True
                if banco[usuario] == senha:
                    achou_senha = True
                    break
        if (achou_senha) and (achou_user):
            print("\n\033[1;32mLogin Efetuado com Sucesso!\033[m")
            print(f"\033[1;32mBem-Vindo {usuario}\033[m")
            return True
        elif not(achou_user):
            msg = ("\033[1;31mUsuário não encontrado\033[m")
        elif not(achou_senha):
            msg = ("\033[1;31mSenha Incorreta, tente novamente...\033[m")
    
    return False   


def menus():
    tipo = ("Livro", "Usuário")
    lista = ("Cadastrar","Atualizar","Pesquisar","Deletar  ")
    
    print()
    for i,e in enumerate(lista):
        #[1] Cadastrar Livro | [5] Cadastrar Usuário
        print(f" {f"[{i+1}] | {e + " " +tipo[0]}":<25}  [{i+1+4}] | {e + " " + tipo[1]}")
    print(f" [9] | Sair\n  >>> ", end= "")


def processar(msg):
    print("\nAguarde um instante processando...")
    sleep(3)
    print(f"\033[1;32m{msg.upper()} REALIZADO COM SUCESSO!\033[m")
