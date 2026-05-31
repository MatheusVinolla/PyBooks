def tela_inicial():
    msg = r"""
     _____                  ____                 _            _      __ _         
    |  __ \                |  _ \               | |          | |    / /| | _
    | |__) | _   _  ______ | |_) |  ___    ___  | | __ ___   |$|   /=/ |@|| | _
    |  ___/ | | | ||______||  _ <  / _ \  / _ \ | |/ // __|  | |  / /  | ||&|| |
    | |     | |_| |        | |_) || (_) || (_) ||   < \__ \  | | / /   | || ||S|
    |_|      \__, |        |____/  \___/  \___/ |_|\_\|___/  |_|/_/    |_||_||_|
              __/ |
             |___/
    """
    print(f"\033[1m{msg}\033[m")
    linha()


def tela_final():
    msg = r"""
    |            .--.   _
    |       .---|__| .((\=.
    |    .--|===|--|/    ,(,
    |    |  |===|  |\      y
    |    |%%|   |  | `.__,'
    |    |%%|   |  | /  \\\
    |    |  |   |  |/|  | \`----.
    |    |  |   |  ||\  \  |___.'_
    |   _|  |   |__||,\  \-+-._.' )_
    |  / |  |===|--|\  \  \      /  \
    | /  `--^---'--' `--`-'---^-'    \
    |'================================`
    """
    print(f"\033[1m{msg}\033[m")
    linha(50)
    print("\n   \033[1;33m M U I T O  ---  O B R I G A D O\033[m")


def construcao():
    msg = r"""
|----------------------------------|        __                       
|                                  |       | \                       
| Desculpe em                      |-------|  \       ______         
| Desenvolvimento                  |       --- \_____/**|_|_\____  | 
|                                  |         \_______ --------- __&gt;-}
|----------------------------------|            /  \_____|_____/   | 
                                               *         |           
                                                            {O}         """
    print(f"\033[1m{msg}\033[m")
    linha()


def menu(*escolhas): #dados em lista
    print()
    for i,e in enumerate(escolhas):
        print(f"  [{i+1}] | {e}")
    print(f"  [{len(escolhas) + 1}] | Sair\n  >>> ", end= "")


def linha(num=70):
    print(f"{'_'*num}")


def continuar():
    print()
    input("\033[1;33mAperte Enter para Continuar...\033[m")


def verificar(num, lista=[]):
    lista.append(lista[-1] + 1)
    while True:
        try:
            num = int(num)
            if (num in lista) or (len(lista) == 0):
                return int(num)
            else:
                num = input("\033[1;31mResposta Inválida, insira novamente >>> \033[m")
        except Exception:
                num = input("\033[1;31mResposta Inválida, insira novamente >>> \033[m")


def limpar():
    from os import system
    system('cls || clear')
    

def modo_local(modo=True):
    from time import sleep
    if modo:  
        linha(50)        
        print("""\033[1;33m
 |          MODO SALVAMENTO LOCAL          |
 |  Atenção os dados não serão salvos      |
 |  posteriormente, apenas sendo aplicados | 
 |  enquanto o programa estiver rodando... |\033[m""")
        linha(50)


#FUNÇÃO EM DESENVOLVIMENTO!
def grafico(): #quantia/produto (dicionario)
    produto = ["A","B","C","D","E"]
    quantia = [20,30,40,50]#50,40,30,20,10
    quantia.sort(reverse=True)
    porcento = []
    for e in quantia():
        porcento.append(e * 100 / sum(quantia))
    maior = porcento[0]
    for e in porcento:
        maior = e if (e > maior) else maior 
        
    for linha in range(maior//10 + 3): 
        for conteudo in range(len(porcento)):
            print(f"\033[{conteudo%7 + 40}m  \033[m", end = " | ")


def creditos():
    linha(50)
    print("""\033[1m
    Sistema de Livraria Py-Book construído como projeto
    da disciplina de Algoritmos e Lógica de Programação
               Ministrada por Flavius Gorgonio
    
    Licença Pública Geral GNU
    www.gnu.org/licenses/gpl.html   
    
    Feito por: Matheus Vínolla Medeiros e Silva  
    Tela Inicial dos Módulos: https://en.rakko.tools/tools/68/
    Tela de Construção: https://ascii-art.botecodigital.dev.br/placas-ascii-art
    Tela de Carrinho: https://emojicombos.com/shopping-cart-ascii-art
    Tela de Livro: https://gemini.google.com/?hl=pt-BR
    Tela Final: https://www.asciiart.eu/books/books\033[m""")
    linha(50)

