from padrao import *
from os import system
from time import sleep

import usuarios
import comprar
import relatorios
import acervo

banco_acervo = {
"123456789": 
{"TITULO":"O Seu Amigo Pateta",
"AUTOR": "Matheus Vínolla",
"ANO": 2020,
"PRECO": 22.50,
"ESTANTE": "INFANTO-JUVENIL",
"TEMAS": "VIOLENCIA"}
}

banco_login = {
"Flavius": "1111",
"Matheus": "0000",
'Joao':"2222"
}

resp = 0
while resp != 6:
    
    tela_inicial()
    menu("Usuários","Acervo de Livros","Comprar", "Relatórios","Sobre o Sistema")
    resp = verificar(input(), [1,2,3,4,5,6])
    limpar()
    local = True
    
    match(resp):
        case 1: #usuarios
            modo_local(local)
            continuar()
            limpar()
            
            usuarios.tela_inicial()
            processo = usuarios.login(banco_login)
            if not(processo):
                for x in range(6):
                    print("\t\033[1;33mS A I N D O\033[m" if x == 0 else "\033[1;33m.\033[m", end="", flush=True)                    
                    sleep(0.35)
            else:
                continuar()
                usuarios.start(banco_acervo)                       
            
            
        case 2: #acervo
            modo_local(local)
            continuar()
            limpar()
            
            acervo.start()
            
            """
            menu2.tela()
            menu2.menu()
            opcao2 = inteiro(input(),[1,2,3,4,5])
            condicoes.menu2(opcao1)
            system('cls || clear')
            menu2.livro(banco_acervo,"123456789")
            continuar()
            """
        case 3: #comprar
            modo_local(local)
            continuar()
            limpar()
                        
            comprar.tela_inicial()
            comprar.menus()
            comprar.condicoes()
        
            
            
        case 4: #relatorio
            modo_local(local)
            continuar()
            limpar()
            
            relatorios.start()
            
        case 5: #sobre o sistema
            creditos()
            continuar()
    limpar()

tela_final()
