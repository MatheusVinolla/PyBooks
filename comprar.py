from padrao import *
def tela_inicial():
    msg = r"""
  _____                                                 _____    _
 / ____|                                               |  __ \  | |
| |       ___   _ __ ___   _ __   _ __   __ _  ___     | |__) |/ __)
| |      / _ \ | '_ ` _ \ | '_ \ | '__| / _` |/ __|    |  _  / \__ \
| |____ | (_) || | | | | || |_) || |   | (_| |\__ \    | | \ \ (   /
 \_____| \___/ |_| |_| |_|| .__/ |_|    \__,_||___/    |_|  \_\ |_|
                          | |
                          |_|
    """
    print(f"\033[1m{msg}\033[m")
    linha()


def carrinho():
    msg = r"""   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⠛⠻⠶⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⢻⣆⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢻⡏⠉⠉⠉⠉⢹⡏⠉⠉⠉⠉⣿⠉⠉⠉⠉⠉⣹⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⣿⣀⣀⣀⣀⣸⣧⣀⣀⣀⣀⣿⣄⣀⣀⣀⣠⡿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⠀⠀⠀⢸⡇⠀⠀⠀⠀⣿⠁⠀⠀⠀⣿⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣧⣤⣤⣼⣧⣤⣤⣤⣤⣿⣤⣤⣤⣼⡏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠀⢸⡇⠀⠀⠀⠀⣿⠀⠀⢠⡿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⠤⠼⠷⠤⠤⠤⠤⠿⠦⠤⠾⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⣷⢶⣶⠶⠶⠶⠶⠶⠶⣶⠶⣶⡶⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⣠⡿⠀⠀⠀⠀⠀⠀⢷⣄⣼⠇⠀⠀⠀⠀⠀"""
    print(f"\033[1m{msg}\033[m")
    linha()


def telao(msg):
    limpar()
    print(f"\033[1;33m <<< MODO {msg.upper()} >>> \033[m")
    

def condicoes():
    opcao = 0
    while (opcao != 5):
        limpar()
        tela_inicial()
        menus()
        opcao = verificar(input(),[1,2,3,4])
        match(opcao):
            case 1:
                telao("catalogo")
                catalogo()
                continuar()
            case 2:
                telao("pesquisa de interesse")
                pesquisa_de_interesse()
            case 3:
                telao("especifico")
                especifico()
                continuar()
            case 4:
                telao("carrinho")
                carrinho()
                print("""
    Seus itens são:
    --Harry Potter e a Pedra Filosofal
    --A Culpa é das Estrelas
    --Intoxicação Digital
    """)
                continuar()


def menus():
    menu("Catálogo","Pesquisa de Interesse","Livro em Específico","Carrinho")


def listar(banco):
    for i,e in (len(banco)//3):
        #0 \t| \t0 | \t0
        print(f"")


def especifico():
    pesq = input("Insira o título do Livro: ")
    print("\033[1;33mLivro Encontrado com Sucesso!\033[m")
    print(r"""
     ________________________
    |_______________________|
    | ::::::::::::::::::::: |
    | ::  _____________  :: |
    | :: |             | :: |
    | :: |   TITULO    | :: |
    | :: |  DO LIVRO   | :: |
    | :: |_____________| :: |
    | ::                 :: |
    | ::                 :: |
    | ::    PY-BOOKS     :: |
    | ::                 :: |
    | ::::::::::::::::::::::|
    |_______________________|
    [_______________________]
    """)


def catalogo():
    l = []
    for x in range(15):
        l.append(x)
    
    l[0]=  " _______________________"
    l[1]=    "|_______________________|"
    l[2]=   "| ::::::::::::::::::::: |"
    l[3]=    "| ::  _____________  :: |"
    l[4]=    "| :: |             | :: |"
    l[5]=    "| :: |   TITULO    | :: |"
    l[6]=    "| :: |  DO LIVRO   | :: |"
    l[7]=    "| :: |_____________| :: |"
    l[8]=   "| ::                 :: |"
    l[9]=    "| ::                 :: |"
    l[10]=    "| ::    PY-BOOKS     :: |"
    l[11]=    "| ::                 :: |"
    l[12]=    "| ::::::::::::::::::::::|"
    l[13]=    "|_______________________|"
    l[14]=    "[_______________________]"
        
    for e in l:
        print(f"{e}\t{e}\t{e}")
    print("[1-3] Pág".center(98))


def pesquisa_de_interesse():
    temas = ["Romance","Infanto-Juvenil","Terror","Bibliografias"]
    for e in temas:
        print(f"\033[1;35mOS MAIS VENDIDOS EM: {e}\033[m")
        catalogo()
        continuar()
        limpar()

