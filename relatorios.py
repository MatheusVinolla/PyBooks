from padrao import *

def tela_inicial():
    msg = r"""
 _____         _         _                 _                   ___ __      ___
|  __ \       | |       | |               (_)                 |  _|\ \    |_  |
| |__) |  ___ | |  __ _ | |_   ___   _ __  _   ___   ___      | |   \ \     | |
|  _  /  / _ \| | / _` || __| / _ \ | '__|| | / _ \ / __|     | |    \ \    | |
| | \ \ |  __/| || (_| || |_ | (_) || |   | || (_) |\__ \     | |     \ \   | |
|_|  \_\ \___||_| \__,_| \__| \___/ |_|   |_| \___/ |___/     | |_     \_\ _| |
                                                              |___|       |___|
    """
    print(f"\033[1m{msg}\033[m")
    linha()


def menus():
    menu("Vendas","Estoque")


def telao(msg):
    limpar()
    tela_inicial()
    print(f"\033[1;33m <<< MODO {msg.upper()} >>> \033[m")


def start(): #condicoes
    opcao = 0
    while (opcao != 3):
        limpar()
        tela_inicial()
        menus()
        opcao = verificar(input(),[1,2])       
        match(opcao):
            case 1: #vendas
                telao("vendas")
                menu("Periodo","Categoria","Maiores/Menores")
                continuar()
            case 2: #estoque
                telao("estoque")
                menu("Total Alfabético", "Categoria")
                continuar()
            

    