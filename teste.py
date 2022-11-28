import os
from FONTES.coresTerminal import cores

menus = ["\b[1 - CADASTRAR UM GASTO]",
         "\b[2 - EXIBIR MEUS GASTOS]",
         "\b[3 - EXCLUIR REGISTRO]",
         "\b[4 - SALVAR EM UM ARQUIVO [EXCEL - TXT]]",
         "\b[5 - ATUALIZAR UM GASTO]",
         "\b[6 - MARCAR GASTO COMO PAGO]",
         "\b[7 - ALTERAR DADOS ANALISADOS]", 
         "\b[8 - SAIR]"
]

def menuOpcoes(descricao):
        os.system("cls")
        print(cores.yellow, '\b--SISTEMA DE CONTROLE DE GASTOS--', cores.reset_color)
        print(cores.green, f'\bGASTO ANALISADO: {descricao}', cores.reset_color)
        for menu in menus:
            print(cores.blue, menu, cores.reset_color)



menuOpcoes(1)