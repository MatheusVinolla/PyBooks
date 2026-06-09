# crud para livraria focada em administração
# crud para livro OK
# estoque OK
# crud para comprar
# -cpf do cliente
# -encontrar livro 
# -deseja comprar? s
# -livro adquirido com sucesso

# relatorio OK
# sair (durante o condicional)
#

#AINDA PRECISO TERMINAR O CRUD DE COMPRAS QUE ESTA INCOMPLETO PARA ESSA TRANSIÇÃO COM DICIONÁRIOS

#ISBN = lista com dados do livro
#titulo,autor,ano,preco,categoria
from os import system

formulario = ['TÍTULO','AUTOR','ANO','PREÇO','CATEGORIA']
estoque_livro = {
'123' : ['Harry Potter', 'JK Rowling','2020','23.34','Infanto-Juvenil'],
'321' : ['Intoxicação digital','August Cury','2022','33.33','Auto-ajuda']
}
historico_compras = {
'123.123.123' : { '123' : ['123','Harry Potter','23.34'],
                  '321' : ['Intoxicação digital','August Cury','2022','33.33','Auto-ajuda']
                }    
}
################################################################

def tela_inicial():
    msg = (r"""
████  █   █      ████   ███   ███  █   █  ████ 
█   █  █ █       █   █ █   █ █   █ █  █  █     
████    █   ████ ████  █   █ █   █ ███    ███  
█       █        █   █ █   █ █   █ █  █      █ 
█       █        ████   ███   ███  █   █ ████  
    """)
    print(f'\033[1;33m{msg}\033[m',end='')

def tela_compra():
    msg = (r"""
 ███   ███  █   █ ████  ████   ███  ████  
█     █   █ ██ ██ █   █ █   █ █   █ █   █ 
█     █   █ █ █ █ ████  ████  █████ ████  
█     █   █ █   █ █     █  █  █   █ █  █  
 ███   ███  █   █ █     █   █ █   █ █   █ 
    """)
    print(f'\033[1;33m{msg}\033[m',end='')

def tela_estoque():
    msg = (r"""
█████  ████ █████  ███   ███  █   █ █████ 
█     █       █   █   █ █   █ █   █ █     
████   ███    █   █   █ █   █ █   █ ████  
█         █   █   █   █ █  █  █   █ █     
█████ ████    █    ███   ██ █  ███  █████ 
    """)
    print(f'\033[1;33m{msg}\033[m',end='')

def tela_cadastrar():
    msg = (r""" _____             _              _                
/  __ \           | |            | |               
| /  \/  __ _   __| |  __ _  ___ | |_  _ __   ___  
| |     / _` | / _` | / _` |/ __|| __|| '__| / _ \ 
| \__/\| (_| || (_| || (_| |\__ \| |_ | |   | (_) |
 \____/ \__,_| \__,_| \__,_||___/ \__||_|    \___/""")
    linha = '_' * 50
    print(f'\033[1m{msg}\n{linha}\n\033[m')

def tela_atualizar():
    msg = (r"""  ___   _                  _  _                                 
 / _ \ | |                | |(_)                                
/ /_\ \| |_  _   _   __ _ | | _  ____  __ _   ___   __ _   ___  
|  _  || __|| | | | / _` || || ||_  / / _` | / __| / _` | / _ \ 
| | | || |_ | |_| || (_| || || | / / | (_| || (__ | (_| || (_) |
\_| |_/ \__| \__,_| \__,_||_||_|/___| \__,_| \___| \__,_| \___/ """)
    linha = '_' * 50
    print(f'\033[1m{msg}\n{linha}\n\033[m')


def tela_pesquisar():
    msg = (r"""______                           _                   
| ___ \                         (_)                  
| |_/ /  ___  ___   __ _  _   _  _  ___   __ _  _ __ 
|  __/  / _ \/ __| / _` || | | || |/ __| / _` || '__|
| |    |  __/\__ \| (_| || |_| || |\__ \| (_| || |   
\_|     \___||___/ \__, | \__,_||_||___/ \__,_||_|   
                      | |                            
                      |_| """)
    linha = '_' * 50
    print(f'\033[1m{msg}\n{linha}\n\033[m')



def tela_deletar():
    msg = (r"""______        _        _                
|  _  \      | |      | |               
| | | |  ___ | |  ___ | |_   __ _  _ __ 
| | | | / _ \| | / _ \| __| / _` || '__|
| |/ / |  __/| ||  __/| |_ | (_| || |   
|___/   \___||_| \___| \__| \__,_||_|""")
    linha = '_' * 50
    print(f'\033[1m{msg}\n{linha}\n\033[m')


def tela_historico():
    msg = (r""" _   _  _       _                 _              
| | | |(_)     | |               (_)             
| |_| | _  ___ | |_   ___   _ __  _   ___   ___  
|  _  || |/ __|| __| / _ \ | '__|| | / __| / _ \ 
| | | || |\__ \| |_ | (_) || |   | || (__ | (_) |
\_| |_/|_||___/ \__| \___/ |_|   |_| \___| \___/ """)
    linha = '_' * 50
    print(f'\033[1m{msg}\n{linha}\n\033[m')


##################################################################
def cadastrar_livro(banco):
    global formulario
    isbn = input('Insira o ISBN do livro para cadastrar: ')
    banco[isbn] = []
    for i,e in enumerate(formulario):
        msg = f'Insira o {formulario[i]} do Livro: '
        banco[isbn].append(input(msg))

def atualizar_livro(banco):
    global formulario
    isbn = input('Insira o ISBN do livro para atualizar: ')
    if isbn in banco:
        print('Livro Encontrado')
        banco[isbn].clear()
        banco[isbn] = []
        for i,e in enumerate(formulario):
            msg = f'Insira o novo {formulario[i]} do Livro: '
            banco[isbn].append(input(msg))
        
    else:
        print('Livro não encontrado, tente novamente...')
    


def pesquisar_livro(banco):
    isbn = input('Insira o ISBN do livro para pesquisar: ')
    if isbn in banco:
        print('Livro Encontrado')
        print()
        for e in banco[isbn]:
            print(e)
        print()
    else:
        print('Livro não encontrado, tente novamente...')


def deletar_livro(banco):
    isbn = input('Insira o ISBN do livro para deletar: ')
    if isbn in banco:
        print('Livro Encontrado')
        del banco[isbn]
        print('Livro deletado com sucesso')
    else:
        print('Livro não encontrado, tente novamente...')
    

##################################################
# -cpf do cliente
# -encontrar livro 
# -deseja comprar? s
# -livro adquirido com sucesso

def cadastrar_compra(livros,banco):
    pessoa = input('Insira o CPF do Cliente que deseja afetuar a compra: ')
    isbn = input('Insira o ISBN do Livro que deseja adquirir: ')
    if isbn in livros:
        print('Livro Encontrado')
        print()
        for e in livros[isbn]:
            print(e)
        print()
        confirmar = input('Deseja adquirir essa obra?')
        if confirmar.upper() == 'S':
                          #BANCO MAIOR
    #'123.123.123' : { '555' : [Harry Potter','23.34']
    #                  '222' : [outra lista de livros]      }
    #'novo' :
            #Banco Livros
    # estoque_livro = {
        #'123' : ['Harry Potter', 'JK Rowling','2020','23.34','Infanto-Juvenil']
        #'321' : ['Intoxicação digital','August Cury','2022','33.33','Auto-ajuda']
         #             } 
        ##############FALTA TERMINAR
            print('Livro Adquirido com sucesso!')
            banco[pessoa] = {}
            banco[pessoa][isbn] = []
            banco[pessoa][isbn].append(livros[isbn][0])
            banco[pessoa][isbn].append(livros[isbn][3])
            print('E cadastrado no seu histórico de compras')
        else:
            print('Ok, estou aqui caso queira...')
    else:
        print('Livro não encontrado...')
    
def historico_compra(banco):
    pessoa = input('Insira o CPF do Cliente que deseja procurar: ')
    if pessoa in banco:
        print('Pessoa Encontrada')
        print()
         #'123.123.123' : { '555' : [Harry Potter','23.34']
        #                  '222' : [outra lista de livros]      }     
        for k,v in banco[pessoa].items():
            print(k,v)
        print()
    else:
        print('Pessoa não encontrada...')

def pesquisar_compra(banco):
    pessoa = input('Insira o CPF do Cliente para ver seu histórico: ')
    if pessoa in banco:
        print('Pessoa Encontrada')
        print()
        isbn = input('Insira o ISBN do livro comprado: ')
        achou = False
        #FAALTA TERMINAR
        #'123.123.123' : { '555' : [Harry Potter','23.34']
        #                  '222' : [outra lista de livros]      }     
        for e in banco[pessoa].keys():
            if e == isbn:
                achou = True
        if achou:
            print(banco[pessoa][isbn])          
        else:
            print('ISBN não encontrado tente novamente...')
        print()
    else:
        print('Livro não encontrado...')
        
    


####################################################
def estoque(banco):
    for k,lista in banco.items():
        print(f' {lista[0]} '.center(30,'='))
        for e in lista:
            if e == lista[0]:
                print(k)
            else:
                print(e)


####################################################
def relatorio():
    print("""\033[1m
FEITO POR: MATHEUS VINOLLA MEDEIROS E SILVA
PROJETO PARA A DISCIPLINA DE ALGORITMOS E 
LOGICA DE PROGRAMAÇÃO
LICENÇA LIVRE GUI\033[m""")

def enter():
    print()
    input('Pressione enter para continuar...') 

def limpar():
    system('cls || clear')
    
#########################################################

def menu():
    tela_inicial()
    msg = input(f"""\033[1;33m
{'='*50}
|  [1] Comprar
|  [2] Estoque
|  [3] Relatórios
|  [4] Sair
|  >>> \033[m""")
    return msg
    
def menu_compra():
    msg = input(f"""\033[1;33m
{'='*50}
|  [1] Nova Compra
|  [2] Histórico
|  [3] Pesquisar
|  [4] Sair
|  >>>\033[m """)
    return msg

def menu_estoque():
    msg = input(f"""\033[1;33m
{'='*50}
|  [1] Cadastrar Livro
|  [2] Pesquisar Livro
|  [3] Atualizar Livro
|  [4] Deletar   Livro
|  [5] Sair
|  >>> \033[m""")
    return msg

#################################################



resp = ''
while resp != '4':
    limpar()
    resp = menu()
    limpar()
    match resp:
        case '1': #COMPRAR
            resp_compra = ''
            while resp_compra != '4':
                limpar()
                tela_compra()
                print('\r\t\n\033[1;33mBem-vindo ao Módulo de Compras\033[m')
                resp_compra = menu_compra()
                limpar()
                match resp_compra:
                    case '1': # NOVA COMPRA
                        tela_cadastrar()
                        cadastrar_compra(estoque_livro,historico_compras)
                        enter()
                    case '2': # HISTORICO
                        tela_historico()
                        historico_compra(historico_compras)
                        enter()
                    case '3': # PESQUISAR
                        tela_pesquisar()
                        pesquisar_compra(historico_compras)
                        enter()
                    case '4': #SAIR
                        print('Sair foi sua escolha')
                        enter()
            
        case '2': #ESTOQUE
            resp_estoque = ''
            while resp_estoque != '5':
                limpar()
                tela_estoque()
                print('\r\t\n\033[1;33mBem-vindo ao Módulo de Estoque\033[m')
                resp_estoque = menu_estoque()
                limpar()
                match resp_estoque:
                    case '1': #CADASTRAR
                        tela_cadastrar()
                        cadastrar_livro(estoque_livro)
                        enter()
                    case '2': #PESQUISAR
                        tela_pesquisar()
                        pesquisar_livro(estoque_livro)
                        enter()
                    case '3': #ATUALIZAR
                        tela_atualizar()
                        atualizar_livro(estoque_livro)
                        enter()
                    case '4': #DELETAR
                        tela_deletar()
                        deletar_livro(estoque_livro)
                        enter()
                    case '5':
                        print('Sair foi sua escolha')
                        enter()
                    
                    case _:
                        print('Resposta Inválida, tente novamente...')
                        enter()

        case '3': #RELATORIO
            relatorio()
            enter()
        case '4': #SAIR
            print('Obrigado e volte sempre!')
        case _: #INVALIDO
            print('Resposta Inválida, tente novamente...')
            enter()
    
    
    
    
    
    