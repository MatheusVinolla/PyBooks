from padrao import *

def tela_inicial():
    msg = r"""
                                                 _  _
    /\                                         _| || |_
   /  \     ___   ___  _ __ __   __  ___      |_  __  _|
  / /\ \   / __| / _ \| '__|\ \ / / / _ \      _| || |_
 / ____ \ | (__ |  __/| |    \ V / | (_) |    |_  __  _|
/_/    \_\ \___| \___||_|     \_/   \___/       |_||_|
    """
    print(f"\033[1m{msg}\033[m")
    linha()

def telao(msg):
    limpar()
    tela_inicial()
    print(f"\033[1;33m <<< MODO {msg.upper()} >>> \033[m")

def start():
    opcao = 0
    while (opcao != 4):
        limpar()
        tela_inicial()
        menus()
        opcao = verificar(input(),[1,2,3]) 
        match(opcao):
            case 1: #título
                telao("título")
                achar_titulo()
                continuar()
            case 2: #ISBN
                telao("isbn")
                achar_isbn()
                continuar()
            case 3: #Categorias
                telao("categorias")
                achar_categorias()
                continuar()
       

def menus():
    menu("Título",'ISBN',"Categorias")


def achar_titulo():
    livro = input("Insira o nome do Livro que deseja procurar: ")
    print("\033[1;32mLivro encontrado!\033[m")
    print("Harry Potter!")


def achar_isbn():
    Isbn = input("Insira o ISBN que deseja procurar: ")
    print("\033[1;32mISBN encontrado!\033[m")
    print("Livro Harry Potter!")


def achar_categorias():
    cat = input("Insira o nome da Categoria que deseja procurar: ")
    print("\033[1;32mCategoria encontrada!\033[m")
    print("Infanto-Juvenil!")