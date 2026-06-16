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

#MANIPULAÇÃO DE ARQUIVOS
##########################################################################################
from time import sleep
from os import system
from arquivos import *

###############################################################################################################
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

def tela_cliente():
    msg = (r"""
 ███  █     ███ █████ █   █ █████ █████  ████ 
█     █      █  █     ██  █   █   █     █     
█     █      █  ████  █ █ █   █   ████   ███  
█     █      █  █     █  ██   █   █         █ 
 ███  █████ ███ █████ █   █   █   █████ ████  
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
        
####################################
#CPF : [cpf,nome,data,email,telefone]
#clientes = {'123.123.123' : ['Nome','28/01/2008','nome@gmail.com','Telefone']

def cadastrar_geral(formulario,banco1,banco2):
    for e in formulario:
        if e == formulario:
            banco1.append(input(f'Insira o {e}: '))    
        else:
            banco2.append(input(f'Insira o {e}: '))
    
    #dessa forma eu evito que todo o loop
    #faça uma verificação

def pesquisar_geral(msg,banco1,banco2):
    alvo = input(f'Insira o {msg} para pesquisar: ')
    if alvo in banco1:
        print(f'{msg} encontrado!')
        for e in banco2[banco1.index(alvo)]:
            print(e)
    else:
        print(f'{msg} não encontrado, tente novamente...')
        
def deletar_geral(msg,banco1,banco2):
    alvo = input(f'Insira {msg} o  do cliente para deletar: ')
    if alvo in banco1:
        print(f'{msg} encontrado!')
        alvo = banco1.index(alvo)
        del banco1[alvo]
        del banco2[alvo]
        print(f'{msg} deletado com sucesso!')
    else:
        print(f'{msg} não encontrado, tente novamente...')

def atualizar_geral(formulario,banco1,banco2):
    alvo = input(f'Insira o {formulario[0]} para atualizar: ')
    if alvo in banco1:
        print(f'{formulario[0]} encontrado!')
        alvo = banco1.index(alvo)
        del banco1[alvo]
        del banco2[alvo]
        
        for e in formulario:
            if e == formulario:
                banco1.append(input(f'Insira o {e} do cliente: '))    
            else:
                banco2.append(input(f'Insira o {e} do cliente: '))
        
    else:
        print(f'{formulario[0]} não encontrado, tente novamente...')

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
|  [3] Clientes
|  [4] Relatórios
|  [5] Sair
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

def menu_cliente():
    msg = input(f"""\033[1;33m
{'='*50}
|  [1] Cadastrar Cliente
|  [2] Pesquisar Cliente
|  [3] Atualizar Cliente
|  [4] Deletar   Cliente
|  [5] Sair
|  >>> \033[m""")
    return msg

#################################################
#MODO DE SALVAMENTO:

#LIVRO (ISBN, DADOS)
l0 = existe_arquivo('estoque_livros.txt')

#CLIENTES (CPF, DADOS)
c0 = existe_arquivo('clientes_dados.txt')

if (l0) and (c0):
    print('Modo Salvamento Externo!')
    externo = True
    enter()
else:
    print('Modo Salvamento Interno!')
    print('Importação de Informações de Teste Importadas!')
    externo = False
    enter()
    
#################################################
#MODO DE TRANSCRIÇÃO

formulario_livros = ['ISBN''TÍTULO','AUTOR','ANO','PREÇO','CATEGORIA']
formulario_clientes = ['CPF','NOME','DATA DE NASCIMENTO','EMAIL','TELEFONE']

#CPF -> ISBN, ISBN
#DESENVOLVIMENTO
historico_compras = {
'123.123.123' : ['123','321'] 
}
#pelo menos 1 ponto e um @

if externo:
    estoque_livros = transcrever_arquivo('estoque_livros.txt')
    clientes_dados = transcrever_arquivo('clientes_dados.txt')
else:
    estoque_livros = {
    '123' : ['Teste1', 'Autor1','2001','12.34','Gênero1'] ,
    '321' : ['Teste2', 'Autor2','2002','43.21','Gênero2']    
    } 
    clientes_dados = {
        '123.123.123' : ['Nome1','20/12/2001','nome1@gmail.com','1234-1234']
        '321.321.321' : ['Nome2','21/11/2002','nome2@gmail.com','4321-4321']
    }

################################33

resp = ''
while resp != '5':
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
                        cadastrar_geral(formulario_livros,estoque_isbn,estoque_livros)
                        if externo:
                            escrita_arquivo(estoque_isbn,estoque_livros,'livros_isbn.txt')
                        enter()
                    case '2': #PESQUISAR
                        tela_pesquisar()
                        pesquisar_geral('Livros',estoque_isbn,estoque_livros)
                        enter()
                    case '3': #ATUALIZAR
                        tela_atualizar()
                        atualizar_geral(formulario_livros,estoque_isbn,estoque_livros)
                        if externo:
                            escrita_arquivo(estoque_isbn,estoque_livros,'livros_isbn.txt')
                        enter()
                    case '4': #DELETAR
                        tela_deletar()
                        deletar_geral('Livros',estoque_isbn,estoque_livros)
                        enter()
                    case '5':
                        print('Sair foi sua escolha')
                        enter()
                    
                    case _:
                        print('Resposta Inválida, tente novamente...')
                        enter()
        
        case '3': #CLIENTES
            resp_cliente = ''
            while resp_cliente != '5':
                limpar()
                tela_cliente()
                print('\r\t\n\033[1;33mBem-vindo ao Módulo de Clientes\033[m')
                resp_cliente = menu_cliente()
                limpar()
                match (resp_cliente):
                    case '1': #CADASTRAR
                        tela_cadastrar()
                        cadastrar_geral(formulario_clientes,clientes_cpf,clientes_dados)
                        if externo:
                            escrita_arquivo(clientes_cpf,clientes_dados,'clientes_cpf.txt','clientes_dados')
                        enter()
                    case '2': #PESQUISAR
                        tela_pesquisar()
                        pesquisar_geral('Cliente',clientes_cpf,clientes_dados)
                        enter()
                    case '3': #ATUALIZAR
                        tela_atualizar()
                        atualizar_geral(formulario_clientes,clientes_cpf,clientes_dados)
                        if externo:
                            escrita_arquivo(clientes_cpf,clientes_dados,'clientes_cpf.txt','clientes_dados')
                        enter()
                    case '4': #DELETAR
                        tela_deletar()
                        deletar_geral('Cliente',clientes_cpf,clientes_dados)
                        enter()
                    case '5': 
                        print('Sair foi sua escolha')
                        enter()
                    case _:  
                        print('Resposta Inválida, tente novamente...')
                        enter()                                  
        case '4': #RELATORIO
            relatorio()
            enter()
    
        case '5':
            print('Obrigado e volte sempre!')
        case _: #INVALIDO
            print('Resposta Inválida, tente novamente...')
            enter()
    
    