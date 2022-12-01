import os
from FONTES.coresTerminal import cores
import BANCO.banco as bd

def pressioneParaContinuar():
    input("Pressione qualquer tecla para continuar... ")
    os.system("cls")


def menuPago():
    print(cores.yellow, 'O GASTO FOI PAGO ? [PADRÃO: NÃO]', cores.reset_color)
    print(cores.blue)
    print('1 - SIM', cores.reset_color)
    print(cores.blue)
    print('2 - NÃO', cores.reset_color)

def init():
    print(cores.green, 'Digite seu saldo atual', cores.reset_color)
    saldo = float(input("..: "))
    print(cores.reset_color)
    pressioneParaContinuar()
    return saldo

def menuGeraArquivo():
    while True:
        try:
            os.system('cls')
            print(cores.blue, '1 - TXT')
            print('2 - EXCEL', cores.reset_color)
            print(cores.yellow)
            op = int(input('Digite uma opcão..: '))
            print(cores.reset_color)

            if op != 1 and op != 2:
                os.system('cls')
                print(cores.red, 'ERRO: DIGITE UMA OPÇÃO VÁLIDA.', cores.reset_color)
                pressioneParaContinuar()
            else:
                break
        except:
            os.system('cls')
            print(cores.red, 'ERRO: DIGITE UMA OPÇÃO VÁLIDA.', cores.reset_color)
            pressioneParaContinuar()  
    return op

def validaID(operacao):
    if operacao == 1:
        try:
            print(cores.yellow, 'Digite o ID do gasto que deseja ATUALIZAR', cores.reset_color)
            id = int(input('..: '))
        except:
            print(cores.red, "ERRO, O ID DIGITADO É INVÁLIDO, TENTE NOVAMENTE COM UM ID VÁLIDO.", cores.reset_color)
            pressioneParaContinuar()
    if operacao == 2:
        try:
            print(cores.yellow, 'Digite o ID do gasto que deseja marcar como pago', cores.reset_color)
            id = int(input('..: '))
        except:
            print(cores.red, "ERRO, O ID DIGITADO É INVÁLIDO, TENTE NOVAMENTE COM UM ID VÁLIDO.", cores.reset_color)
            pressioneParaContinuar()
            
    return id

def menuTipoDado():
    print(cores.yellow)
    print('--ESCOLHA OS GASTOS PARA AS OPERAÇÕES--', cores.yellow)
    print(cores.blue)
    print('1 - TODOS OS GASTOS')
    print('2 - GASTOS PAGOS')
    print('3 - GASTOS NÃO PAGOS')
    print('4 - GASTOS DIA 5')
    print('5 - GASTOS DIA 15', cores.reset_color)
    
    print(cores.yellow, 'DIGITE A OPÇÃO', cores.reset_color)
    op = input('..: ')
    
    nomeOpcao = [None] * 2
    nomeOpcao[0] = op
    while True:
        match op:
            case '1':
                nomeOpcao[1] = 'TODOS OS GASTOS'
                break
            case '2':
                nomeOpcao[1] = 'GASTOS PAGOS'
                break
            case '3':
                nomeOpcao[1] = 'GASTOS NÃO PAGOS'
                break
            case '4':
                nomeOpcao[1] = ' GASTOS DIA 5'
                break
            case '5':
                nomeOpcao[1] = 'GASTOS DIA 15'
                break
            case _:
                print('OPÇÃO INVÁLIDA')
    return nomeOpcao
    
def tipoDataFrame(op):
    while True:
        match op:
            case '1':
                DADOS = bd.buscaTudo()
                break
            case '2':
                DADOS = bd.buscaPago()
                break
            case '3':
                DADOS = bd.buscaNaoPago()
                break
            case '4':
                DADOS = bd.buscaDia5()
                break
            case '5':
                DADOS = bd.buscaDia15()
                break
            case _:
                print(cores.red, 'OPÇÃO INVÁLIDA', cores.red)
                
    pressioneParaContinuar()
    return DADOS
